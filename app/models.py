from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    high_bid = db.Column(db.Integer, unique=True)
    low_ask = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<Item: {}>'.format(self.name)    