from flask import render_template, request, redirect, url_for
from flask_login import  current_user

from sqlalchemy.sql import text

from application import app, db, login_required
from application.auth.models import User
from application.users.forms import UserForm
from application.items.models import Item

@app.route("/users/new", methods=["GET"])
def user_create_form():
    return render_template("users/new.html", form = UserForm())


@app.route("/users/", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    return render_template("users/list.html", users=User.query.all())

@app.route("/users/privilege/<user_id>", methods=["POST"])
@login_required(role="ADMIN")
def set_user_privilege(user_id):
    user = User.query.get(user_id)
    if user.roles() == "ADMIN":
        user.role =  "BASIC" 
    else:
        user.role =  "ADMIN" 
    db.session().commit()

    return redirect(url_for("users_index"))


@app.route("/user/", methods=["GET","POST"])
def user_create():
    form = UserForm(request.form)

    if request.method == "GET":
        return render_template("users/new.html", form = UserForm())


    if not form.validate():
        return render_template("users/new.html", form = form)

    u = User(username=request.form.get("username"),
             password=request.form.get("password"),
             name=request.form.get("name"))


    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/remove/user/<user_id>", methods=["POST"])
@login_required(role="ANY")
def remove_user(user_id):
    user = User.query.get(user_id)

    if user.id != current_user.id:
        stmt = text('''DELETE FROM Item
                       WHERE Item.account_id = :userId;'''
                    ).params(userId=user.id)
        res = db.engine.execute(stmt)

        db.session().delete(user)
        db.session().commit()
    
    
    return redirect(url_for("users_index"))
