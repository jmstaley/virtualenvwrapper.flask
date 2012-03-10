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
                           'Flask-WTF'])
    subprocess.check_call(['touch', 
                           '%s.py' % project,
                           'forms.py',
                           'models.py'])
    subprocess.check_call(['mkdir', 'templates', 'static'])
    return
