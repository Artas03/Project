from Applications import app, db
from Applications.models import Maintenance

@app.route('/')
@app.route('/home')
def Home():
    return 'This is the home page'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    form = RegisterForm

    if request.method == 'POST':
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
        elif len(number) < 10 or len(number) > 10:
            error = "Invalid Phone number"
        else:
            return f"Thank You {forename} {surname}"
    return render_template('registerform.html', form=form, message=error)

@app.route('/add-vehicle', methods=['GET', 'POST'])
def add-vehicle():
    error = ""
    form = MaintenanceForm

    if request.method == 'POST':
        make = form.make.data
        model = form.model.data
        year = form.year.data

        if len(make) == 0 or len(model) == 0:
            error = "Please enter the Make and Model of your vehicle"
        elif len(year) = 0:
            error = "Please enter the year of your vehicle"
        else:
            return f"Thak You, the vehicle: {year} {make} {model} has been added"
    
    return render_template('maintenance.html', form=form, message=error)
@app.route('/update/<name>')


