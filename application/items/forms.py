from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ItemForm(FlaskForm):
    name = StringField("Item name", [validators.length(min=2,max=30)])
    available = BooleanField("Available")
    
 
    class Meta:
        csrf = False