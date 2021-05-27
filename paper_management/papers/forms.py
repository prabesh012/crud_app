from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, FileField
from wtforms.validators import ValidationError

ALLOWED_EXTENSIONS = {'pdf'}

class AddForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    publish_date = DateField('Published Date')
    category = StringField('Category')
    research_file = FileField('Research Paper')
    submit = SubmitField('Submit')

    def validate_research_file(self,field):
        print(field.data.filename)
        if not ('.' in field.data.filename and field.data.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS):
            raise ValidationError('File is not pdf')  

class DelForm(FlaskForm):
    id = IntegerField()
    submit = SubmitField("Delete")

class UpdateForm(FlaskForm):
    id = IntegerField()
    title = StringField('Title')
    author = StringField('Author')
    publish_date = DateField('Published Date')
    category = StringField('Category')
    research_file = FileField('Research Paper')
    submit = SubmitField('Update')

    def validate_research_file(self,field):
        print(field.data)
        print(type(field.data))
        print(field.data.filename)
        if not ('.' in field.data.filename and field.data.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS):
            raise ValidationError('File is not pdf')  
