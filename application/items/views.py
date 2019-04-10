from flask import redirect, render_template, request, url_for
from flask_login import  current_user

from application import app, db, login_required
from application.items.models import Item
from application.items.forms import ItemForm 

from application.category.models import Category

@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())


@app.route("/items/new")
@login_required(role="ANY")
def items_form():
    form = ItemForm(available=True)
    categories = []

    queredCategories = Category.query.all()

    for category in queredCategories:
        categories.append((category.id, category.category_type))
    form.category.choices = categories

    return render_template("items/new.html", form = form)
        
@app.route("/items/<item_id>", methods=["POST"])
@login_required(role="ANY")
def items_set_availability(item_id):
    item = Item.query.get(item_id)
    item.available = not item.available
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/remove/<item_id>", methods=["POST"])
@login_required(role="ANY")
def remove_item(item_id):
    item = Item.query.get(item_id)
    print(current_user)
    if item.account_id == current_user.id:
        db.session().delete(item)
        db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/borrow/<item_id>", methods=["POST"])
@login_required(role="ANY")
def borrow_item(item_id):
    item = Item.query.get(item_id)
    item.borrowed = True
    item.borrowed_by_id = current_user.id
    item.available = False
    db.session().add(item)
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
@login_required(role="ANY")
def items_create():
    form = ItemForm(request.form)
    print(form.validate())

    ## validation doesn't work anymore.
    '''
    if not form.validate():
        return render_template("items/new.html", form = form)
    '''

    item = Item(form.name.data)
    item.available = form.available.data
    item.account_id = current_user.id
    item.category_id = form.category.data


    db.session().add(item)
    db.session().commit()
  
    return redirect(url_for("items_index"))