from application import db

from sqlalchemy.sql import text
from sqlalchemy import event

class Category(db.Model):

    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)

    category_type = db.Column(db.String(144), nullable=False)

    item = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, category_type):
        self.category_type = category_type 
  
    def get_type(self):
        return self.category_type
