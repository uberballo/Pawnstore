from flask import render_template
from application import app
from application.auth.models import User
from application.items.models import Item

@app.route("/")
def index():
    return render_template("index.html", items_available=User.find_all_available_items(),items_count=Item.count_all_available_items_for_each_category())
