from Applications import db
from Applications.models import Customers, Maintenance

db.drop_all()
db.create_all()
