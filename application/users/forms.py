from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class UserForm(FlaskForm):
    username = StringField("Username",[validators.length(min=2)])
    password = PasswordField("Password") 

    class Meta:
        csrf = False