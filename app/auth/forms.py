from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length


class LoginForm(FlaskForm):
	username = StringField('用户名',
		validators=[InputRequired(message='用户名不能为空')], 
		render_kw={"placeholder":"用户名"})
	password = PasswordField('密码',
		validators=[InputRequired(message='密码不能为空')], 
		render_kw={"placeholder":"密码"})
	loginsubmit = SubmitField('确定')


class RegForm(FlaskForm):
	regusername = StringField('用户名', 
		validators=[InputRequired(message='用户名不能为空'),
					Length(min=4,max=20,message='用户名必须介于4-20字符'),], 
		render_kw={"placeholder":"用户名"})
	regpassword = PasswordField('密码',
		validators=[InputRequired(message='密码不能为空'),
					Length(min=4,max=20,message='密码必须介于4-20字符'),], 
		render_kw={"placeholder":"密码"})
	confirmpassword = PasswordField('重复密码',
		validators=[InputRequired(message='重复密码不能为空'),
					EqualTo('regpassword',message='重复密码与密码输入不一致')], 
		render_kw={"placeholder":"请再输入一次密码"})
	regsubmit = SubmitField('注册')
	
	
class ModifyForm(FlaskForm):
	oldpassword = PasswordField('旧密码',
		validators=[InputRequired(message='旧密码不能为空'),
					Length(min=4,max=20,message='密码必须介于4-20字符'),], 
		render_kw={"placeholder":"旧密码"})
	newpassword = PasswordField('新密码',
		validators=[InputRequired(message='新密码不能为空'),
					Length(min=4,max=20,message='密码必须介于4-20字符'),], 
		render_kw={"placeholder":"新密码"})
	confirmnewpassword = PasswordField('重复新密码',
		validators=[InputRequired(message='重复新密码不能为空'),
					Length(min=4,max=20,message='密码必须介于4-20字符'),
					EqualTo('newpassword',message='重复新密码与新密码输入不一致')], 
		render_kw={"placeholder":"请再输入一次新密码"})
	modifysubmit = SubmitField('确定')
	
	
	
	
	
	
	
	
