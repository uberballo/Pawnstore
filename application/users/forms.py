from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class UserForm(FlaskForm):
    username = StringField("Username"
    ,[validators.length(min=2,max=30)])
    password = PasswordField("Password",[validators.InputRequired()
    ,validators.EqualTo('confirm',message= 'Passwords must match')])
    confirm = PasswordField('Repeact password')

    class Meta:
        csrf = False