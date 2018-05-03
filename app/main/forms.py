from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, FormField, FieldList
from wtforms.validators import InputRequired, ValidationError, Length
#~ from flask import flash
			
	
class CalssifyAddForm(FlaskForm):
	classify_add_name = StringField('分类名', 
		validators=[InputRequired(message='分类名不能为空'),
					Length(max=20,message='分类名不能超过20字符'),], 
		render_kw={"placeholder":"分类名"})
	classify_add_submit = SubmitField('确定')
					

class NoteAddForm(FlaskForm):
	note_add_name = StringField('分类名', 
		validators=[InputRequired(message='分类名不能为空'),
					Length(max=20,message='分类名不能超过20字符'),], 
		render_kw={"placeholder":"分类名"})
	note_add_submit = SubmitField('确定')
	
			
						
			
			
			
			
			
			
			
			
			

