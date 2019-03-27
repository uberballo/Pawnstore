from application import db
from application.models import Base

class Item(Base):

    __tablename__ = "item"

    name = db.Column(db.String(144), nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
     nullable=False)
    

    def __init__(self, name):
        self.name = name
        self.available= True 
        self.borrowedBy = "temp"
