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
    subprocess.check_all(['pip', 'install', 'Flask'])
    return
