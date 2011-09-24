from __future__ import with_statement
import sys, os

from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn, task

from fabric.contrib.console import confirm
from fabric.contrib.files import upload_template 
import StringIO
import tempfile

env.project_name = 'brownie'
env.server_name_template = 'brownie.%(host)s'

env.deploy_user = 'django_%s' % env.project_name
env.settings_module = '%s.settings.deploy' % env.project_name

env.project_repository = 'git://github.com/RaphaelKimmig/brownie.git'

env.project_base_dir = '/srv/django/'
env.project_dir = os.path.join(env.project_base_dir, env.project_name)
env.virtualenv_dir = os.path.join(env.project_dir, 'env')

env.media_root = '/media/'
env.static_root = '/media/static/'

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

def config_from_template(template, config, context):
    fd, tmp_file = tempfile.mkstemp()
    get(template, local_path=tmp_file)
    with open(tmp_file, 'r') as f:
        t = f.read()
        print t, context
        t = t % context
    with open(tmp_file, 'w') as f:
        f.write(t)

    put(tmp_file, config, use_sudo=True)


def copy_configs():
    uwsgi_template = os.path.join(env.project_dir, 'deploy/configs/uwsgi.ini')
    uwsgi_config = '/etc/uwsgi/apps-enabled/%s.ini' % env.project_name
    uwsgi_context = {
        'project_name': env.project_name, 
        'project_dir': env.project_dir,
        'env': env.virtualenv_dir,
        'settings_module': env.settings_module
        }
    config_from_template(uwsgi_template, uwsgi_config, uwsgi_context)

    nginx_template = os.path.join(env.project_dir, 'deploy/configs/nginx.conf')
    nginx_config = '/etc/nginx/sites-enabled/%s.conf' % env.project_name
    nginx_context = {
        'project_dir': env.project_dir,
        'project_name': env.project_name, 
        'server_name': env.server_name_template % {'host' : env.host},
        'static_root': env.static_root,
        'media_root': env.media_root,
        }
    config_from_template(nginx_template, nginx_config, nginx_context)

@task
def deploy():
    try:
        sudo("useradd %(user)s -d %(home)s -U" % {'user': env.deploy_user, 'home': env.project_dir})
    except:
        warn("user %s already exists" % env.deploy_user)

    if os.path.exists(env.project_dir):
        warn("Project dir %s already exists" % env.project_dir)
        with cd(env.project_dir):
            sudo('git pull', user=env.deploy_user)
    else:
        with cd(env.project_base_dir):
            sudo("git clone %s" % env.project_repository)
            sudo("chown -R %(user)s:%(user)s %(directory)s" % {'user':
                env.deploy_user, 'directory': env.project_dir})

    for dir in ('logs', 'public'):
        full_dir = os.path.join(env.project_dir, dir)
        if not os.path.exists(full_dir):
            sudo("mkdir %s" % full_dir, user=env.deploy_user)

    sudo("virtualenv --no-site-packages %s" % env.virtualenv_dir,
            user=env.deploy_user)
    sudo("pip install -E %(env)s -r %(req)s" % {'env': env.virtualenv_dir,
        'req': os.path.join(env.project_dir, 'deploy/requirements.txt')},
        user=env.deploy_user)

    copy_configs()
    sudo('service uwsgi reload')
    sudo('service nginx reload')


@task 
def update():
    pass

# def vagrant():
#     # change from the default user to 'vagrant'
#     env.user = 'vagrant'
#     # connect to the port-forwarded ssh
#     env.hosts = ['127.0.0.1:2222']
# 
#     # use vagrant ssh key
#     env.key_filename = '/usr/lib/ruby/gems/1.8/gems/vagrant-0.7.5/keys/vagrant'
#     env.code_dir = '/srv/django/pdm/'
#     env.virtualenv_dir = '/srv/django/pdm/env'
#     env.base_dir = '/srv/django/pdm/env'
#     env.activate = '/srv/django/pdm/env/bin/activate'
#     env.requirements = '/srv/django/pdm/pdm/requirements.txt'
# 
# def production():
#     env.user = 'vagrant'
#     env.hosts = ['127.0.0.1:2222']
#     env.key_filename = '/usr/lib/ruby/gems/1.8/gems/vagrant-0.7.5/keys/vagrant'
# 
#     env.code_dir = '/srv/eb2.0.proclima.com/pdm/'
#     env.virtualenv_dir = '/srv/eb2.0.proclima.com/pdm/env'
#     env.base_dir = '/srv/eb2.0.proclima.com/pdm/env'
#     env.activate = '/srv/eb2.0.proclima.com/pdm/env/bin/activate'
#     env.requirements = '/srv/eb2.0.proclima.com/pdm/pdm/requirements.txt'
# 
# def install_apt_deps():
#     sudo("apt-get update")
#     sudo("apt-get build-dep python-imaging -y")
#     sudo("apt-get install imagemagick")
# 
# def refresh_virtualenv():
#     install_apt_deps()
#     with settings(warn_only=True):
#         if run("test -d %s" % env.virtualenv_dir).failed:
#             run("virtualenv %s --no-site-packages" % env.virtualenv_dir)
# 
#     virtualenv("pip install -U -r %s" % env.requirements)
# 
# def virtualenv(command):
#     run("source %s && %s" % (env.activate, command))
# 
# def push():
#     #local("git commit -a")
#     local("git push")
# 
# def deploy():
#     push()
#     with settings(warn_only=True):
#         if run("test -d %s" % env.code_dir).failed:
#             cloned = True
#             run("git clone raphael@ampad.de:/var/git/projects/pdm %s" % env.code_dir)
# 
#     with cd(env.code_dir):
#         if not 'cloned' in locals():
#             run("git pull")
# 
# 
