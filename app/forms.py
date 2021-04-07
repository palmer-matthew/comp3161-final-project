from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField,IntegerField, TextAreaField, SelectMultipleField, SubmitField, PasswordField, RadioField
from wtforms.validators import Email,DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    match = RadioField('Search Options', validators=[DataRequired()], choices=[('recipe', 'Recipe'),('plan', 'Meal Plan')])

class addRecipe(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])   
    calorie_count = IntegerField('Calorie Count', validators=[DataRequired()])
    serving = IntegerField('Serving', validators=[DataRequired()])
    prep_time = IntegerField('Prep Time', validators=[DataRequired()])
    image = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])
