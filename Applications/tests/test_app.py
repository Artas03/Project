from flask import url_for
from flask_testing import TestCase

from Applications import app, db
from Applications.models import Customers, Maintenance
from Applications import models, app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app 

    def setUp(self):
        db.create_all()
        sample1 = Customers(forename="Kamran",
        surname = "Singh",
        email = "kamransingh@hotmail.com",
        number = "07576776153")
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('read_customers'))
        self.assert200(response, "Could not load read customers page")

class TestViews(TestBase):
    def test_get_read(self):
        response = self.client.get(url_for('read_vehicle'))
        self.assert200(response, "Could not load read customers page")






