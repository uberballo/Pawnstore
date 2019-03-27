from application import db

class Category(db.Model):

    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)

    item = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name