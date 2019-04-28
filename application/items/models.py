from application import db
from application.models import Base

from sqlalchemy.sql import text

class Item(Base):

    __tablename__ = "item"

    name = db.Column(db.String(144), nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
     nullable=False)

    borrowed = db.Column(db.Boolean, nullable = True)
    borrowed_by_id = db.Column(db.Integer, nullable = True)
    

    def __init__(self, name):
        self.name = name
        self.available= True

    @staticmethod
    def count_all_available_items_for_each_category():
        stmt = text('''SELECT COUNT(Item.id), Category.category_type
                       FROM Item
                       LEFT JOIN Category ON Item.category_id = Category.id
                       GROUP BY Category.category_type
                       ORDER BY COUNT(Item.id) DESC;''')
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"count":row[0], "name":row[1]})
        
        return response