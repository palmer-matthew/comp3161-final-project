from flask_wtf import FlaskForm
from wtforms.fields import StringField,IntegerField, TextAreaField, SelectMultipleField, SubmitField
from wtforms.validators import Email,DataRequired
from flask_wtf.file import FileAllowed, FileRequired, FileField


class addRecipe(FlaskForm):
    
    recipe_name = StringField('Recipe Name')
    
    calorie_count = IntegerField('Calorie Count')
    
    serving = IntegerField('Serving')
    
    prep_time = IntegerField('Prep Time')
    
    image = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])
    
    ingredients = SelectMultipleField(u'Ingredients', choices=[('cpp', 'Carrots'), ('py', 'Plums'), ('text', 'Something Else')])

    # ingredients = SelectMultipleField('Ingredients', choices=[('crr', Carrot), ('lt', 'Lettuce), ('or', 'Orange'), ('pl', 'plums)] )
    
    instructions = StringField('Instructions')
    
    add = SubmitField('Add')
    