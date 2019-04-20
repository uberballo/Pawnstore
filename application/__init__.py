#flask 
from flask import Flask
app = Flask(__name__)

import os

#database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listen
from sqlalchemy import event
from sqlalchemy.sql import text

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:   
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

#Login
#from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

#We initiliaze a not logged in user.
from application.auth.anonymous import Anonymous
login_manager.anonymous_user = Anonymous

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
from application import views


#Items
from application.items import models
from application.items import views 

from application.category import models



#We insert few categories to the category table. 
def insert_data(target, connection, **kw):
    connection.execute(target.insert(),
    {'category_type':'Animal'},
    {'category_type':'Food'})

    
event.listen(models.Category.__table__, 'after_create',insert_data)
from application.auth import models
from application.auth import views

from application.users import views


from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    insert_initial_values()
except: 
    pass
