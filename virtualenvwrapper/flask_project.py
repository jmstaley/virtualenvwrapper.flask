#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012 Jon Staley
#
""" Create Flask project automatically with virtualenvwrapper
"""

import logging
import subprocess
import os

log = logging.getLogger('virtualenvwrapper.flask')

def template(args):
    """ Installs Flask
    """
    project = args[0]
    subprocess.check_call(['pip', 
                           'install', 
                           'Flask', 
                           'Flask-login',
                           'Flask-SQLAlchemy',
                           'Flask-WTF',
                           'Flask-Script'])

    # setup project directories
    subprocess.check_call(['mkdir', '%s' % project])
    subprocess.check_call(['mkdir', 
                           '%s/templates' % project, 
                           '%s/static' % project])
    
    # setup project files
    data_files = '%s/data' % os.path.abspath(os.path.dirname(__file__))

    manage_file = open('manage.py', 'w')
    init_file = open('%s/__init__.py' % project, 'w')

    subprocess.check_call(['touch', 
                           '%s/forms.py' % project,
                           '%s/models.py' % project,
                           '%s/views.py' % project])

    files = [(manage_file, '%s/manage.py' % data_files),
             (init_file, '%s/__init__.py' % data_files)]
    create_files(files, project)

    return

def create_files(files, project):
    for f, name in files:
        subprocess.check_call(['sed',
                               's/\[APPNAME\]/%s/' % project, 
                               '%s' % name],
                               stdout=f)
        f.close()
                               
