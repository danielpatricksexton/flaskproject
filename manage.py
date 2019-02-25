from app import db
from run import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        print('SQLite detected')
        migrate = Migrate(app, db, render_as_batch=True)
    else:
        print(db.engine.url.drivername)
        migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
