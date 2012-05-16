import config

from models import db
from views import login_manager, [APPNAME]

from flask import Flask

def create_app(database_uri=''):                                                                                                                 
    app = Flask(__name__)
    app.config.from_object(config)

    # overrides if passed in
    if database_uri:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    login_manager.setup_app(app)
    db.init_app(app)
    app.register_blueprint([APPNAME])

    return app

