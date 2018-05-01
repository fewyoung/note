from . import main
from .forms import ClassifyForm, AddForm#, DelForm
from flask import render_template, request, redirect, url_for#~ from flask import session, flash
from flask_login import login_required, current_user
from ..models import db, Classify


#添加分类表单、所有分类表单列表
def add_classify_forms():		
	user_id = current_user.get_id()		
	#无分页查询
	#classify_forms = []
	#~ classifies = Classify.query.filter_by(user_id=user_id).order_by(Classify.id.desc())	
	#~ for classify in classifies:	
		#~ classify_form_temp = ClassifyForm()	
		#~ classify_form_temp.classify_name.data = classify.classify_name
		#~ classify_form_temp.classify_id.data = classify.id
		#~ classify_forms.append(classify_form_temp)		
	#分页查询
	page = request.values.get('page', default=8, type=int)
	pagination = Classify.query.filter_by(
		user_id=user_id).order_by(
		Classify.id.desc()).paginate(
		page, per_page=3,error_out=False)
	page_items = pagination.items	
	add_form = AddForm()	
	#~ return (add_form,classify_forms)
	return (add_form, pagination)


#添加分类表单、所有分类表单列表、所有笔记表单列表、内容表单
def add_classify_article_content_forms():
	add_form, pagination = add_classify_forms()	
	article_forms = []
	content_form = None		
	return (add_form, pagination, article_forms, content_form)


@main.route('/note', methods=['GET', 'POST'])
@login_required
def note():	
	(add_form,
	pagination,
	article_forms,
	content_form) = add_classify_article_content_forms()
	return render_template('note.html', add_form = add_form,
							pagination = pagination,
							article_forms = article_forms,
							content_form = content_form)
	

@main.route('/note/classify', methods=['GET', 'POST'])
@login_required
def classify():
	#删除分类
	del_id = request.values.get('del_id')
	if del_id:
		classify_del = Classify.query.filter_by(id = del_id).first()
		if classify_del:
			db.session.delete(classify_del)
			db.session.commit()
	add_form = AddForm()		
	#新增分类，未检测分类名
	user_id = current_user.get_id()
	add_name = request.values.get('add_name')
	#ajax提交表单，判断button的data值失效	
	#if add_form.add_submit.data and add_form.validate_on_submit():
	#ajax只提交数据，无法通过validate
	#if add_name:
	if add_name and add_form.validate_on_submit():	
		classify_add = Classify()
		classify_add.classify_name = add_name
		classify_add.user_id = user_id
		db.session.add(classify_add)
		db.session.commit()	
	#必须放在最后，否则不是删除或者增加后的查询结果
	add_form, pagination = add_classify_forms()
	return render_template('classify.html',
							add_form = add_form,
							pagination = pagination)
							














