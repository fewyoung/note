from . import main
from .forms import ClassifyForm, AddForm#, DelForm
from flask import render_template, request, redirect, url_for#~ from flask import session, flash
from flask_login import login_required, current_user
from ..models import db, Classify


@main.route('/note', methods=['GET', 'POST'])
@login_required
def note():
	user_id = current_user.get_id()
						
	#删除分类	
	classify_form = ClassifyForm()
	if classify_form.del_submit.data and classify_form.validate_on_submit():
		del_classify = Classify.query.filter_by(
			id = classify_form.classify_id.data).first()
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
		classify_form_temp.classify_submit.label.text = classify.classify_name
		classify_form_temp.classify_id.data = classify.id
		classify_forms.append(classify_form_temp)
		
	return render_template('note.html',
							add_form=add_form,
							classify_forms=classify_forms)


@main.route('/note/del', methods=['GET', 'POST'])
@login_required
def del_note():
	del_id = request.values.get('del_id')
	classify_del = Classify.query.filter_by(id = del_id).first()
	if classify_del:
		db.session.delete(classify_del)
		db.session.commit()
	else:
		pass	
	return redirect(url_for('main.note'))
	#~ return "true"







