from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import db
from .forms import LoginForm, PurchaseItemForm, RegisterForm, SellItemForm
from .models import Item, User
from .utils import logout_required


@app.route("/")
@app.route("/home/")
def home_page():
    return render_template("home.html")


@app.route("/market/", methods=["GET", "POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        # Purchase Item Logic
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(
                    f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price_formatted}",
                    category="success",
                )
            else:
                flash(
                    f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!",
                    category="danger",
                )
        # Sell Item Logic
        sold_item = request.form.get("sold_item")
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(
                    f"Congratulations! You sold {s_item_object.name} back to market!",
                    category="success",
                )
            else:
                flash(
                    f"Something went wrong with selling {s_item_object.name}",
                    category="danger",
                )

        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = Item.query.filter_by(owner_id=None)
        owned_items = Item.query.filter_by(owner_id=current_user.id)
        return render_template(
            "market.html",
            items=items,
            purchase_form=purchase_form,
            owned_items=owned_items,
            selling_form=selling_form,
        )


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
