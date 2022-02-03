from stockCollector import db

class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f"<Stock: {self.name}, {self.price}, {self.time}>"
