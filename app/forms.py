from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired



class ContactForm(FlaskForm):
    Username = StringField('username', validators=[DataRequired()])
    Password = StringField('password', validators=[DataRequired()])
   
