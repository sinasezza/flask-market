from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Float, nullable=False, default=1000.99)
    items = db.relationship("Item", backref="owner", lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    barcode = db.Column(db.String(length=12), unique=True, nullable=False)
    description = db.Column(db.String(length=1024), nullable=True)
    price = db.Column(db.Float(), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item('{self.name}', '{self.barcode}', '{self.description}', '{self.price}')"
