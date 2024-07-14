from flask import current_app as app
from flask import render_template


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/market/")
def market_page():
    items = [
        {"id": 1, "name": "Chocolate Sandwich Cookies", "barcode": "CCO12345", "description": "Cookie", "price": 0.12},
        {"id": 2, "name": "Spinach Artichokes", "barcode": "ART45678", "description": "Artichoke", "price": 0.25},
        {"id": 3, "name": "Lemon Pies", "barcode": "PIP99999", "description": "Lemon Pie", "price": 1.99},
        {"id": 4, "name": "Chocolate Cake", "barcode": "CAK77777", "description": "Chocolate", "price": 3.45},
    ]
    return render_template("market.html", items=items)