import os
from app import create_app, db
from app.models import User#~ from app.models import User, Registration_Lan, Registration_Wan
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('IP_REGISTER_CONFIG') or 'development')

migrate = Migrate(app, db)

def make_shell_context():
	return dict(app=app, db=db, User=User)

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
