from . import auth
from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required


@auth.route('/', methods=['GET', 'POST'])
def login():
	login_form = LoginForm()
	if login_form.submit.data:
		if login_form.username.data == '' or login_form.password.data == '':
			flash('错误：用户名或密码不能为空')	
	if login_form.submit.data and login_form.validate_on_submit():
		user = User.query.filter_by(username=login_form.username.data).first()
		if user is not None and user.verify_password(login_form.password.data):
			login_user(user)
			next = request.args.get('next')
			if next is None or not next.startswith('/'):
				next = url_for('main.index')
			return redirect(next)
		flash('错误：无效的用户名或密码')
	return render_template('auth/login.html', login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('您已经退出')
	return redirect(url_for('auth.login'))
