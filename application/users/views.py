from flask import render_template, request, redirect, url_for
from application import app, db
from application.auth.models import User
from application.users.forms import UserForm

@app.route("/users/", methods=["GET"])
def user_create_form():
    return render_template("users/new.html", form = UserForm())

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
