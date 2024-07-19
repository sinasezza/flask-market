from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user


def logout_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated:
            flash("you should logout to do this operation", category="warning")
            return redirect(url_for("home_page"))

        return func(*args, **kwargs)

    return decorated_view
