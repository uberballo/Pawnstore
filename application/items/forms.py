from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, BooleanField, validators

class ItemForm(FlaskForm):
    name = StringField("Item name", [validators.length(min=2,max=30)])
    available = BooleanField("Available")
    category = SelectField("Category",choices=[])
    
 
    class Meta:
        csrf = False