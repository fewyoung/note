from . import auth
from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegForm
from ..models import User, db
from flask_login import login_user, logout_user, login_required


@auth.route('/', methods=['GET', 'POST'])
def login():
	#~ 注册表单处理
	reg_form = RegForm()
	if reg_form.regsubmit.data:
		if reg_form.regusername.data == '' or reg_form.regpassword.data == '':
			flash('错误：用户名与密码不能为空')
		if len(reg_form.regusername.data) < 4 or len(reg_form.regpassword.data) > 20:
			flash('错误：用户名与密码须介于4-20字符')
		if reg_form.regpassword.data != reg_form.confirmpassword.data:
			flash('错误：重复密码与密码输入不一致')
	if reg_form.regsubmit.data and reg_form.validate_on_submit():
		user = User()
		user.username = reg_form.regusername.data
		user.password = reg_form.regpassword.data
		db.session.add(user)
		db.session.commit()
		flash('恭喜您，注册成功！')
		return redirect(url_for('auth.login'))	
		
	#~ 登录表单处理
	login_form = LoginForm()
	if login_form.loginsubmit.data:
		if login_form.username.data == '' or login_form.password.data == '':
			flash('错误：用户名或密码不能为空')	
	if login_form.loginsubmit.data and login_form.validate_on_submit():
		user = User.query.filter_by(username=login_form.username.data).first()
		if user is not None and user.verify_password(login_form.password.data):
			login_user(user)
			next = request.args.get('next')
			if next is None or not next.startswith('/'):
				next = url_for('main.index')
			return redirect(next)
		flash('错误：无效的用户名或密码')
		
	return render_template('auth/login.html',
							login_form=login_form,
							reg_form=reg_form)
	

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('您已经退出')
	return redirect(url_for('auth.login'))
