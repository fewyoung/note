from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
	username = StringField('用户名', validators=[InputRequired(message='用户名不能为空')], 
		render_kw={"placeholder":"用户名"})
	password = PasswordField('密码', validators=[InputRequired(message='密码不能为空')], 
		render_kw={"placeholder":"密码"})
	submit = SubmitField('确定')
