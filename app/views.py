from flask import current_app as app
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import db
from .forms import LoginForm, RegisterForm
from .models import Item, User
from .utils import logout_required


@app.route("/")
@app.route("/home/")
def home_page():
    return render_template("home.html")


@app.route("/market/")
@login_required
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register/", methods=["GET", "POST"])
@logout_required
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data,
        )
        db.session.add(user)
        db.session.commit()

        flash("Your account has been created! please login", category="info")
        return redirect(url_for("login_page"))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error: {err_msg}", category="error")

    return render_template("register.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
@logout_required
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password_correction(form.password.data):
            login_user(user)
            flash(f"Welcome {user.username}", category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Invalid username or password", category="error")

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error: {err_msg}", category="error")
    return render_template("login.html", form=form)


@app.route("/logout/")
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out", category="info")
    return redirect(url_for("login_page"))
