from __future__ import with_statement
import sys, os

from fabric.api import abort, cd, env, get, hide, hosts, local, prompt, \
    put, require, roles, run, runs_once, settings, show, sudo, warn, task

from fabric.contrib.console import confirm

PROJECT_NAME = 'brownie'
DEPLOY_USER = 'django_brownie'
PROJECT_BASE_DIR = '/srv/'
PROJECT_DIR = os.path.join(PROJECT_BASE_DIR, PROJECT_NAME)
PROJECT_REPOSITORY = 'https://github.com/RaphaelKimmig/brownie.git'

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

def setup_base():
    try:
        sudo("useradd %(user)s -d %(home)s -U" % {'user': DEPLOY_USER, 'home': PROJECT_DIR})
    except:
        pass

@task
def deploy():
    setup_base()

    with cd(PROJECT_BASE_DIR):
        sudo("git clone %s" % PROJECT_REPOSITORY)
        sudo("chown -R %(user)s:%(user)s %(directory)s" % {'user': DEPLOY_USER,
            'directory': PROJECT_DIR})

    with cd(PROJECT_DIR):
        sudo("virtualenv --no-site-packages env", user=DEPLOY_USER)
        sudo("pip install -E env -r %s" % 'deploy/requirements.txt', user=DEPLOY_USER)
        
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
