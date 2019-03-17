from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username",[validators.length(min=2)])
    password = PasswordField("Password")

    class Meta:
        csrf = False