from flask import Blueprint, render_template, request, flash, redirect,\                                                                         
    url_for

from flaskext.login import LoginManager

login_manager = LoginManager()

[APPNAME] = Blueprint('[APPNAME]', __name__,
                     template_folder='templates')  
