from . import main
from .forms import ClassifyForm, AddForm, DelForm
from flask import render_template#~ from flask import render_template, session, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models import db, Classify


@main.route('/note', methods=['GET', 'POST'])
@login_required
def index():
	user_id = current_user.get_id()
						
	#删除分类
	del_form = DelForm()
	if del_form.del_submit.data and del_form.validate_on_submit(): 
		del_classify = Classify.query.filter_by(
			id = del_form.del_id.data).first()
		db.session.delete(del_classify)
		db.session.commit()	
											
	#新分类,未检测同名
	add_form = AddForm()	
	if add_form.add_submit.data and add_form.validate_on_submit(): 
		add_classify = Classify()
		add_classify.classify_name = add_form.add_name.data
		add_classify.user_id = user_id
		db.session.add(add_classify)
		db.session.commit()
		add_form.add_name.data = ''

	#当前用户所有分类列表，必须放在最后，否则删除或新增后必须刷新页面	
	classify_forms = []
	classifies = Classify.query.filter_by(user_id=user_id).order_by(Classify.id.desc())	
	for classify in classifies:	
		classify_form_temp = ClassifyForm()	
		del_form_temp = DelForm()
		classify_form_temp.classify_submit.label.text = classify.classify_name
		del_form_temp.del_classify.data = classify.classify_name
		del_form_temp.del_id.data = classify.id
		classify_forms.append([classify_form_temp,del_form_temp])
		
	return render_template('main.html',
							classify_forms=classify_forms,
							add_form=add_form)










