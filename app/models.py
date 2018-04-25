from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, index = True)
	password_hash = db.Column(db.String(20))
	user_classifies = db.relationship('Classify', backref='user')

	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute!')
		
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password) 
		
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))	
	
	def __repr__(self):
		return '<User %r>' % self.username


class Classify(db.Model):
	__tablename__ = 'classifies'
	id = db.Column(db.Integer, primary_key = True)
	classify_name = db.Column(db.String(20))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	
	def __repr__(self):
		return '<Classify %r>' % self.classify_name


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

