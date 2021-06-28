from werkzeug.utils import html
from Applications import app, db
from Applications.models import Maintenance, Customers
from flask import render_template, request, redirect, url_for 
from Applications.forms import CustomersForm, MaintenanceForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    form = CustomersForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            forename = form.forename.data
            surname = form.surname.data
            email = form.email.data
            number = form.number.data

            if len(forename) == 0 or len(surname) == 0:
                error = "Please enter a First name and Surname"
            elif len(email) == 0:
                error = "Please enter an E-mail address"
            elif len(number) == 0:
                error = "Please enter a Phone Number"
            elif len(number) < 10 or len(number) > 11:
                error = "Invalid Phone number"
            else:
                allocate = Customers(forename = forename, surname = surname, email = email, number = number)
                db.session.add(allocate)
                db.session.commit()
                return f"Thank You {forename} {surname}"
    return render_template("registerform.html", form=form, message=error)

@app.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    error = ""
    form = MaintenanceForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            make = form.make.data
            model = form.model.data
            year = form.year.data

            if len(make) == 0 or len(model) == 0:
                error = "Please enter the Make and Model of your vehicle"
            elif len(year) == 0:
                error = "Please enter the year of your vehicle"
            else:
                allocate1 = Maintenance(make = make, model = model, year = year)
                db.session.add(allocate1)
                db.session.commit()
                return f"Thank You, the vehicle: {year} {make} {model} has been added"
    
    return render_template('maintenance.html', form=form, message=error)


@app.route('/update_customer/<int:id>', methods=["GET", "POST"])
def update_customer(id):
    form = CustomersForm()
    object = Customers.query.filter_by(id=id).first()
    if request.method == "POST":
        if form.validate_on_submit():
            object.forename = form.forename.data
            object.surname = form.surname.data
            object.email = form.email.data
            object.number = form.number.data
            db.session.add
            db.session.commit()
            return f" Customer has been updated"
    return render_template('updatecustomer.html', form=form)

@app.route('/update_vehicle/<int:maintenance_id>', methods=["GET", "POST"])
def update_vehicle(maintenance_id):
    form = MaintenanceForm()
    object = Maintenance.query.filter_by(maintenance_id=maintenance_id).first()
    if request.method == "POST":
        if form.validate_on_submit():
            object.make = form.make.data
            object.model = form.model.data
            object.year = form.year.data
            db.session.add
            db.session.commit()
            return f" Vehichle has been updated"
    return render_template('updatemaintenance.html', form=form)

@app.route('/read_customers', methods = ['GET'])
def read_customers():
    if request.method == 'GET':
        all_customers = Customers.query.all()
        customerstring = ""
        for customer in all_customers:
            customerstring += "<br>" + customer.forename
    return customerstring

@app.route('/read_vehicle', methods = ['GET'])
def read_vehicle():
    if request.method == 'GET':
        all_vehicles = Maintenance.query.all()
        vehiclestring = ""
        for vehicle in all_vehicles:
            vehiclestring += f"<br>  {vehicle.make}  {vehicle.model}  {vehicle.year}"
    return vehiclestring 

@app.route('/delete_customers/<int:id>')
def delete_customers(id):
    customer_delete = Customers.query.get(id)
    db.session.delete(customer_delete)
    db.session.commit()
    return 'Customer deleted'

@app.route('/delete_vehicles/<int:maintenance_id>')
def delete_vehicles(maintenance_id):
    vehicle_delete = Maintenance.query.get(maintenance_id)
    db.session.delete(vehicle_delete)
    db.session.commit()
    return 'Vehicle deleted'