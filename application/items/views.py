from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.items.models import Item
from application.items.forms import ItemForm 


@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new")
@login_required
def items_form():
    return render_template("items/new.html", form = ItemForm(available=True))

@app.route("/items/<item_id>", methods=["POST"])
@login_required
def items_set_availability(item_id):
    item = Item.query.get(item_id)
    item.available = not item.available
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/remove/<item_id>", methods=["POST"])
@login_required
def remove_item(item_id):
    item = Item.query.get(item_id)
    db.session().delete(item)
    db.session().commit()

    return redirect(url_for("items_index"))


@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)


    ##Nyt lisätään temp category_id, pitää korjata että käyttäjä voi lisätä itse
    ## formissa ei voi valita vielä
    item = Item(form.name.data)
    item.available = form.available.data
    item.account_id = current_user.id


    db.session().add(item)
    db.session().commit()
  
    return redirect(url_for("items_index"))