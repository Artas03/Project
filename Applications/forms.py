from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError 

from Applications.models import Customers, Maintenance


class CustomersForm(FlaskForm):
    forename = StringField('First Name: ', validators=[
        DataRequired(),
        Length(min=2,max=20)
        ])
    surname = StringField('Last Name: ', validators=[
        DataRequired(),
        Length(min=2,max=20)
        ])
    email = StringField('E-mail Address: ', validators=[
        DataRequired(),
        Email()
        ])
    number = StringField('Contact Number: ', validators=[
        DataRequired(),
        Length(min=11,max=11)
        ])
    submit = SubmitField('Add Customer')


class MaintenanceForm(FlaskForm):
    make = StringField('Make of vehicle: ', validators=[
        DataRequired(),
        Length(min=2,max=20)
        ])
    model = StringField('Model of vehicle: ', validators=[
        DataRequired(),
        Length(min=2,max=20)
        ])
    year = StringField('Year of vehicle: ', validators=[
        DataRequired(),
        Length(min=3,max=4)
        ])
    submit = SubmitField('Add Vehicle')
