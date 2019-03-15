from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    borrowedBy = db.Column(db.String(100), nullable=True)

    def __init__(self, name):
        self.name = name
        self.available= True 
        self.borrowedBy = "temp"
