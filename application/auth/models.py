from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
    

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    items = db.relationship("Item", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    #Currently users are all basic. 
    def roles(self):
        return ["BASIC"]


    @staticmethod
    def find_all_available_items():
        stmt = text("SELECT Item.name FROM Item"
                    " WHERE Item.available = '1'")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            print(row)
            response.append({"name":row[0] })

        return response