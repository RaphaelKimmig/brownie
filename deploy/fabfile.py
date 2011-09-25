from __future__ import with_statement
import sys, os

from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn, task

from fabric.contrib.console import confirm
from fabric.contrib.files import upload_template, contains
import StringIO
import tempfile

env.project_name = 'brownie'
env.server_name_template = 'brownie.%(host)s'

env.deploy_user = 'www-data'
env.settings_module = '%s.settings.local' % env.project_name

env.project_repository = 'git://github.com/RaphaelKimmig/brownie.git'

env.project_base_dir = '/srv/django'
env.project_dir = os.path.join(env.project_base_dir, env.project_name)
env.virtualenv_dir = os.path.join(env.project_dir, 'env')

env.media_root = '/media'
env.static_root = '/media/static'

env.config_scheme = 'configs/default/%(config)s'
env.per_host_config_scheme = 'configs/hosts/%(host)s/%(config)s'

def get_uwsgi_data():
    target = '/etc/uwsgi/apps-enabled/%s.xml' % env.project_name
    virtualen_lib = sudo("find %s -mindepth 3 -maxdepth 3 -type d -name\
            'site-packages'" % env.virtualenv_dir, user=env.deploy_user).splitlines()[-1]
    context = {
        'project_name': env.project_name, 
        'project_dir': env.project_dir,
        'env': virtualen_lib,
        'settings_module': env.settings_module,
        'user': env.deploy_user,
        }
    return {'target': target, 'context': context}

def get_nginx_data():
    target = '/etc/nginx/sites-enabled/%s.conf' % env.project_name
    context = {
        'project_name': env.project_name, 
        'project_dir': env.project_dir,
        'server_name': env.server_name_template % {'host' : env.host},
        'static_root': env.static_root,
        'media_root': env.media_root,
        }
    return {'target': target, 'context': context}

def get_django_data():
    target = os.path.join(env.project_dir, env.project_name,
            'settings/local.py') 
    return {'target': target, 'chown': '%s:%s' % (env.deploy_user, env.deploy_user)}

env.configs = {
        'uwsgi.xml': get_uwsgi_data,
        'nginx.conf': get_nginx_data,
        'django_settings.py': get_django_data 
}


def check_dependencies(dependencies):
    missing = []
    for dependency in dependencies:
        try:
            exec('import %s' % dependency)
        except ImportError:
            missing.append(dependency)
    return missing

@task
def bootstrap_dev():
    local("virtualenv --no-site-packages ../env")
    local("pip install -E ../env -r %s" % '../requirements.txt')

def django_command(cmd):
    activate = os.path.join(env.virtualenv_dir, 'bin/activate')
    return sudo("source %(activate)s && django-admin.py %(cmd)s \
            --settings=%(settings)s --pythonpath=%(path)s" % { 'cmd':
                cmd, 'activate': activate, 'settings': env.settings_module,
                'path': env.project_dir}, user=env.deploy_user)


def copy_configs():
    for config, data in env.configs.items():
        per_host_file = env.per_host_config_scheme % {'host': env.host,
                'config': config}
        generic_file = env.config_scheme % {'host': env.host,
                'config': config}

        if os.path.exists(per_host_file):
            config_file = per_host_file
        elif os.path.exists(generic_file):
            config_file = generic_file
        else:
            warn("No config file found for %s (tried %s and %s)" % (config,
                per_host_file, generic_file))
            continue
        with open(config_file, 'r') as config_file:
            if callable(data):
                data = data()

            config_content = config_file.read()

            if 'context' in data:
                config_content = config_content % data['context']
            
            if not 'target' in data:
                warn("No target specified for config %s" % config)
                continue

            put(StringIO.StringIO(config_content), data['target'], use_sudo=True)

            if 'chown' in data:
                sudo('chown %s %s' % (data['chown'], data['target']))




@task
def deploy():
    if not contains('/etc/passwd', env.deploy_user):
        sudo("useradd %(user)s -d %(home)s -U" % {'user': env.deploy_user, 'home': env.project_dir})

    if os.path.exists(env.project_dir):
        warn("Project dir %s already exists" % env.project_dir)
        with cd(env.project_dir):
            sudo('git reset --hard', user=env.deploy_user)
            sudo('git pull', user=env.deploy_user)
    else:
        with cd(env.project_base_dir):
            sudo("git clone %s" % env.project_repository)
            for dir in ('logs', 'public', 'media/static', 'media/dynamic'):
                full_dir = os.path.join(env.project_dir, dir)
                sudo("mkdir -p %s" % full_dir)
            sudo("chown -R %(user)s:%(user)s %(directory)s" % {'user':
                env.deploy_user, 'directory': env.project_dir})
            sudo("chmod 750 %s" % env.project_dir)

    if not os.path.exists(env.virtualenv_dir):
        sudo("virtualenv --no-site-packages %s" % env.virtualenv_dir,
                user=env.deploy_user)
    sudo("pip install -E %(env)s -r %(req)s" % {'env': env.virtualenv_dir,
        'req': os.path.join(env.project_dir, 'deploy/requirements.txt')},
        user=env.deploy_user)

    copy_configs()

    django_command('syncdb')
    django_command('migrate')
    django_command('collectstatic --noinput')

    sudo('service uwsgi reload')
    sudo('service nginx reload')

@task 
def update():
    pass
