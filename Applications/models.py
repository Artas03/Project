from Applications import db

class Customers(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    number = db.Column(db.String(11), unique=True, nullable=False)
    verified = db.Column(db.Boolean, default=False)

class Maintenance(db.Model):
    maintenance_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    service = db.Column(db.DateTime, nullable=False)
    mot = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeingKey(Customers.customer_id))