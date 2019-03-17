from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.items.forms import ItemForm 


@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new")
def items_form():
    return render_template("items/new.html", form = ItemForm(available=True))

@app.route("/items/<item_id>", methods=["POST"])
def items_set_availability(item_id):
    t = Item.query.get(item_id)
    t.available = not t.available
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)

    t = Item(form.name.data)
    t.available = form.available.data


    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("items_index"))