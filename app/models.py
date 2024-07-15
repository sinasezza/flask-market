from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    barcode = db.Column(db.String(length=12), unique=True, nullable=False)
    description = db.Column(db.String(length=1024), nullable=True)
    price = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f"Item('{self.name}', '{self.barcode}', '{self.description}', '{self.price}')"
