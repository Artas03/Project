from sqlalchemy.orm import backref
from Applications import db

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    forename = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(11), nullable=False)
    relationship = db.relationship('Maintenance', backref = 'Customers')

class Maintenance(db.Model):
    maintenance_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)    
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey(Customers.id))