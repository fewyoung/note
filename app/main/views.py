from . import main
from .forms import CalssifyAddForm, TitleAddForm
from flask import render_template, request, redirect, url_for#~ from flask import session, flash
from flask_login import login_required, current_user
from ..models import db, Classify, Note


#分类区域：[添加分类表单,所有分类的分页对象]
def classify_area(classify_page):		
	user_id = current_user.get_id()			
	#分页对象	
	classify_pagination = Classify.query.filter_by(
		user_id=user_id).order_by(
		Classify.id.desc()).paginate(
		classify_page, per_page=10,error_out=False)
	classify_add_form = CalssifyAddForm()	
	return (classify_add_form,
			classify_pagination)


#标题区域：[添加标题表单,所有标题的分页对象]
def title_area(classify_id, title_page):				
	#分页对象
	if classify_id:	
		title_pagination = Note.query.filter_by(
			classify_id=classify_id).order_by(
			Note.id.desc()).paginate(
			title_page, per_page=10,error_out=False)
	else:
		title_pagination = None
	title_add_form = TitleAddForm()	
	return (title_add_form,
			title_pagination)


@main.route('/note', methods=['GET', 'POST'])
@login_required
def note():	
	classify_add_form, classify_pagination = classify_area(classify_page=1)
	title_add_form, title_pagination = title_area(classify_id = None, title_page = 1)
	content_form = None							
	return render_template('note.html',
							classify_add_form = classify_add_form,
							classify_pagination = classify_pagination,
							title_add_form = title_add_form,
							title_pagination = title_pagination,
							content_form = content_form)
	

@main.route('/note/classify', methods=['GET', 'POST'])
@login_required
def classify():
	#删除分类
	classify_del_id = request.values.get('classify_del_id')
	if classify_del_id:
		classify_del = Classify.query.filter_by(id = classify_del_id).first()
		if classify_del:
			db.session.delete(classify_del)
			db.session.commit()
	#新增分类，未检测分类名
	classify_add_form = CalssifyAddForm()		
	user_id = current_user.get_id()
	classify_add_name = request.values.get('classify_add_name')
	#ajax提交表单，判断button的data值失效	
	#if add_form.add_submit.data and add_form.validate_on_submit():
	#ajax只提交数据，不进行validate
	if classify_add_name and classify_add_form.validate_on_submit():	
		classify_add = Classify()
		classify_add.classify_name = classify_add_name
		classify_add.user_id = user_id
		db.session.add(classify_add)
		db.session.commit()	
	classify_page = request.values.get('classify_page_id', default=1, type=int)
	#必须放在最后，否则不是删除或者增加后的查询结果
	classify_add_form, classify_pagination = classify_area(classify_page)
	return render_template('classify.html',
							classify_add_form = classify_add_form,
							classify_pagination = classify_pagination)
							

@main.route('/note/title', methods=['GET', 'POST'])
@login_required
def title():
	#删除标题
	title_del_id = request.values.get('title_del_id')
	if title_del_id:
		title_del = Note.query.filter_by(id = title_del_id).first()
		if title_del:
			db.session.delete(title_del)
			db.session.commit()
	#新增标题，未检测标题
	title_add_form = TitleAddForm()
	classify_id = request.values.get('classify_id')
	title_add_name = request.values.get('title_add_name')
	if title_add_name and title_add_form.validate_on_submit():	
		title_add = Note()
		title_add.note_title = title_add_name
		title_add.classify_id = classify_id
		db.session.add(title_add)
		db.session.commit()
	title_page = request.values.get('title_page_id', default=1, type=int)
	#必须放在最后，否则不是删除或者增加后的查询结果
	title_add_form, title_pagination = title_area(classify_id, title_page)
	return render_template('title.html',
							title_add_form = title_add_form,
							title_pagination = title_pagination)









