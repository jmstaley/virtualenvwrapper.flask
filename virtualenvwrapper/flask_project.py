#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012 Jon Staley
#
""" Create Flask project automatically with virtualenvwrapper
"""

import logging
import subprocess

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
    subprocess.check_call(['touch', 
                           '%s/__init__.py' % project,
                           '%s/forms.py' % project,
                           '%s/models.py' % project,
                           'manage.py'])
    return
