from flaskext.script import Manager
from testing import create_app, db

app = create_app()
manager = Manager(app)

@manager.command
def initdb():
    """ create all database tables """
    with app.test_request_context():
        db.create_all()

@manager.command
def dropdb():
    """ drops all database tables """
    with app.test_request_context():
        db.drop_all()

if __name__ == "__main__":
    manager.run()
