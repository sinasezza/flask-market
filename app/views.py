from flask import current_app as app
from flask import flash, get_flashed_messages, redirect, render_template, url_for

from .forms import RegisterForm
from .models import Item, User, db


@app.route("/")
@app.route("/home/")
def home_page():
    return render_template("home.html")


@app.route("/market/")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register/", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password1.data,
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login_page"))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error: {err_msg}", category="error")

    return render_template("register.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login_page():
    return render_template("login.html")
