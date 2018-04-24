from . import auth
from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegForm, ModifyForm
from ..models import User, db
from flask_login import login_user, logout_user, login_required, current_user


@auth.route('/', methods=['GET', 'POST'])
def login():			
	login_form = LoginForm()
	if login_form.loginsubmit.data and login_form.validate_on_submit():
		user = User.query.filter_by(username=login_form.username.data).first()
		if user is not None and user.verify_password(login_form.password.data):
			login_user(user)
			next = request.args.get('next')
			if next is None or not next.startswith('/'):
				next = url_for('main.index')
			return redirect(next)
		else:
			login_form.password.errors.append('无效的用户名或密码')
	return render_template('auth/login.html',login_form=login_form)		


@auth.route('/reg', methods=['GET', 'POST'])
def reg():
	reg_form = RegForm()
	if reg_form.regsubmit.data and reg_form.validate_on_submit():
		user = User()
		user.username = reg_form.regusername.data
		user.password = reg_form.regpassword.data
		db.session.add(user)
		db.session.commit()
		flash('恭喜您，注册成功！')
		return redirect(url_for('auth.login'))
	return render_template('auth/reg.html',reg_form=reg_form)
							

@auth.route('/modify', methods=['GET', 'POST'])
@login_required
def modify():
	modify_form = ModifyForm()
	if modify_form.modifysubmit.data and modify_form.validate_on_submit():	
		user = current_user	
		if not user.verify_password(modify_form.oldpassword.data):
			modify_form.oldpassword.errors.append('旧密码输入错误')
		else:
			user.password = modify_form.newpassword.data
			db.session.add(user)
			db.session.commit()
			flash('恭喜您，密码修改成功，请重新登录！')
			logout_user()
			return redirect(url_for('auth.login'))
	return render_template('auth/modify.html',modify_form=modify_form)

	
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('您已经退出')
	return redirect(url_for('auth.login'))
