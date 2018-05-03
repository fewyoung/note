from . import main
from .forms import CalssifyAddForm, NoteAddForm
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


#日志名称区域：[添加日志名称表单,所有日志名称的分页对象]
def note_area(classify_id, note_page):				
	#分页对象
	if classify_id:	
		note_pagination = Note.query.filter_by(
			classify_id=classify_id).order_by(
			Note.id.desc()).paginate(
			note_page, per_page=10,error_out=False)
	else:
		note_pagination = None
	note_add_form = NoteAddForm()	
	return (note_add_form,
			note_pagination)


#所有区域
def all_area(classify_page, classify_id, note_page):
	classify_add_form, classify_pagination = classify_area(classify_page)	
	note_add_form, note_pagination = note_area(classify_id, note_page)	
	content_form = None		
	return (classify_add_form,
			classify_pagination,
			note_add_form,
			note_pagination,
			content_form)


@main.route('/note', methods=['GET', 'POST'])
@login_required
def note():	
	classify_add_form, classify_pagination = classify_area(classify_page=1)
	(classify_add_form,
		classify_pagination,
		note_add_form,
		note_pagination,
		content_form) = classify_area(classify_page=1,
										classify_id=None,
										note_page=1)								
	note_add_form, note_pagination = note_area(classify_id, note_page) 							
	return render_template('note.html',
							classify_add_form = classify_add_form,
							classify_pagination = classify_pagination,
							article_forms = article_forms,
							content_form = content_form)
	

@main.route('/note/classify', methods=['GET', 'POST'])
@login_required
def classify():
	#删除分类
	del_id = request.values.get('classify_del_id')
	if del_id:
		classify_del = Classify.query.filter_by(id = del_id).first()
		if classify_del:
			db.session.delete(classify_del)
			db.session.commit()
	#新增分类，未检测分类名
	classify_add_form = CalssifyAddForm()		
	user_id = current_user.get_id()
	classify_add_name = request.values.get('classify_add_name')
	#ajax提交表单，判断button的data值失效	
	#if add_form.add_submit.data and add_form.validate_on_submit():
	#ajax只提交数据，无法通过validate
	if classify_add_name and classify_add_form.validate_on_submit():	
		classify_add = Classify()
		classify_add.classify_name = classify_add_name
		classify_add.user_id = user_id
		db.session.add(classify_add)
		db.session.commit()	
	classify_page = request.values.get('classify_page_id', default=1, type=int)
	#必须放在最后，否则不是删除或者增加后的查询结果
	classify_add_form, pagination = classify_area(classify_page)
	return render_template('classify.html',
							classify_add_form = classify_add_form,
							classify_pagination = classify_pagination)
							














