from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, FormField, FieldList
from wtforms.validators import InputRequired, ValidationError, Length
#~ from flask import flash
			
	
class ClassifyForm(FlaskForm):
	classify_id = HiddenField('id')
	classify_name = StringField('分类名')
	del_submit = SubmitField('删除')	
	
	
class AddForm(FlaskForm):
	add_name = StringField('分类名', 
		validators=[InputRequired(message='分类名不能为空'),
					Length(max=20,message='分类名不能超过20字符'),], 
		render_kw={"placeholder":"分类名"})
	add_submit = SubmitField('确定')
					

	
			
						
			
			
			
			
			
			
			
			
			

