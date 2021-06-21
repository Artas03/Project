from Applications import app, db
from Applications.models import Maintenance

@app.route('/')
@app.route('/home')
def Home():
    return 'This is the home page'