from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField

class AddForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    publish_date = DateField('Published Date')
    category = StringField('Category')
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    id = IntegerField()
    submit = SubmitField("Delete")

class UpdateForm(FlaskForm):
    id = IntegerField()
    title = StringField('Title')
    author = StringField('Author')
    publish_date = DateField('Published Date')
    category = StringField('Category')
    submit = SubmitField('Update')