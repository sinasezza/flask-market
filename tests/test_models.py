import os
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from app import app, db, bcrypt
from app.models import User, Item

# Set the configuration for testing
os.environ['FLASK_CONFIGURATION'] = 'testing'

@pytest.fixture(scope='module')
def new_user():
    user = User(username='testuser', email='testuser@example.com', password='password123', budget=1000.99)
    return user

@pytest.fixture(scope='module')
def new_item():
    item = Item(name='Test Item', barcode='123456789012', price=100.0)
    return item

@pytest.fixture(scope='module')
def test_client():
    # Re-initialize the app with the test configuration
    app.config.from_object('configuration.TestingConfig')

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()

def test_new_user(new_user):
    assert new_user.username == 'testuser'
    assert new_user.email == 'testuser@example.com'
    assert new_user.password != 'password123'  # Password should be hashed
    assert new_user.budget == 1000.99

def test_check_password_correction(new_user):
    assert new_user.check_password_correction('password123')
    assert not new_user.check_password_correction('wrongpassword')

def test_budget_formatted(new_user):
    assert new_user.budget_formatted == '1,000.99$'

def test_can_purchase(new_user, new_item):
    new_user.budget = 200.0
    assert new_user.can_purchase(new_item)
    new_user.budget = 50.0
    assert not new_user.can_purchase(new_item)

def test_can_sell(new_user, new_item):
    new_user.items.append(new_item)
    assert new_user.can_sell(new_item)
    new_user.items.remove(new_item)
    assert not new_user.can_sell(new_item)

def test_new_item(new_item):
    assert new_item.name == 'Test Item'
    assert new_item.barcode == '123456789012'
    assert new_item.price == 100.0

def test_price_formatted(new_item):
    assert new_item.price_formatted == '100.00$'

def test_buy_item(test_client, new_user, new_item):
    new_user.budget = 200.0
    new_item.buy(new_user)
    assert new_item.owner_id == new_user.id
    assert new_user.budget == 100.0

def test_sell_item(test_client, new_user, new_item):
    new_user.budget = 100.0
    new_item.sell(new_user)
    assert new_item.owner_id is None
    assert new_user.budget == 200.0
