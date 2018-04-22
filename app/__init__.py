from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config
#~ from flask_login import LoginManager


db = SQLAlchemy()
bootstrap = Bootstrap()
#~ login_manager = LoginManager()
#~ login_manager.session_protection = 'strong'
#~ login_manager.login_view = 'auth.login'
#~ login_manager.login_message = '请您登录后访问此页面'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	
	db.init_app(app)
	bootstrap.init_app(app)
	#~ login_manager.init_app(app)
	
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	#~ from .auth import auth as auth_blueprint
	#~ app.register_blueprint(auth_blueprint)
	
	return app
