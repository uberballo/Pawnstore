from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item

@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new")
def items_form():
    return render_template("items/new.html")

@app.route("/items/<item_id>", methods=["POST"])
def items_set_availability(item_id):
    t = Item.query.get(item_id)
    t.available = not t.available
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
def items_create():
    t = Item(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("items_index"))