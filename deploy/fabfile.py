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
env.settings_module = '%s.settings.deploy' % env.project_name

env.project_repository = 'git://github.com/RaphaelKimmig/brownie.git'

env.project_base_dir = '/srv/django/'
env.project_dir = os.path.join(env.project_base_dir, env.project_name)
env.virtualenv_dir = os.path.join(env.project_dir, 'env')

env.media_root = '/media'
env.static_root = '/media/static'

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

def config_from_template(template, config, context):
    fd, tmp_file = tempfile.mkstemp()
    get(template, local_path=tmp_file, use_sudo=True)
    with open(tmp_file, 'r') as f:
        t = f.read()
        t = t % context
    with open(tmp_file, 'w') as f:
        f.write(t)

    put(tmp_file, config, use_sudo=True)


def copy_configs():
    uwsgi_template = 'configs/uwsgi.xml'
    uwsgi_config = '/etc/uwsgi/apps-enabled/%s.xml' % env.project_name
    virtualen_lib = sudo("find %s -mindepth 3 -maxdepth 3 -type d -name\
            'site-packages'" % env.virtualenv_dir, user=env.deploy_user).splitlines()[-1]
    uwsgi_context = {
        'project_name': env.project_name, 
        'project_dir': env.project_dir,
        'env': virtualen_lib,
        'settings_module': env.settings_module,
        'user': env.deploy_user,
        }
    upload_template(uwsgi_template, uwsgi_config, uwsgi_context, use_sudo=True,
            backup=False)

    nginx_template = 'configs/nginx.conf'
    nginx_config = '/etc/nginx/sites-enabled/%s.conf' % env.project_name
    nginx_context = {
        'project_dir': env.project_dir,
        'project_name': env.project_name, 
        'server_name': env.server_name_template % {'host' : env.host},
        'static_root': env.static_root,
        'media_root': env.media_root,
        }
    upload_template(nginx_template, nginx_config, nginx_context, use_sudo=True,
            backup=False)

@task
def deploy():
    if not contains('/etc/passwd', env.deploy_user):
        sudo("useradd %(user)s -d %(home)s -U" % {'user': env.deploy_user, 'home': env.project_dir})

    if os.path.exists(env.project_dir):
        warn("Project dir %s already exists" % env.project_dir)
        with cd(env.project_dir):
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

    django_command('syncdb')
    django_command('migrate')
    django_command('collectstatic')



    copy_configs()

    sudo('service uwsgi reload')
    sudo('service nginx reload')

@task 
def update():
    pass
