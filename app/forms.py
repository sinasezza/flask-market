from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

from .models import User


class RegisterForm(FlaskForm):
    username = StringField(
        label="Username:",
        validators=[DataRequired("You must have username"), Length(min=2, max=30)],
    )
    email = StringField(
        label="Email:",
        validators=[
            DataRequired("You must have email"),
            Email(),
            Length(min=5, max=100),
        ],
    )
    password1 = PasswordField(
        label="Password:", validators=[DataRequired(), Length(min=6)]
    )
    password2 = PasswordField(
        label="Confirm Password:",
        validators=[DataRequired(), Length(min=6), EqualTo("password1")],
    )
    submit = SubmitField(label="Submit")

    def validate_username(self, username_to_check: str) -> User:
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please try a different username"
            )
        return user

    def validate_email(self, email_to_check: str) -> User:
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("Email already exists! Please try a different email")
        return user


# =======================================================================================

class LoginForm(FlaskForm):
    username = StringField(
        label="Username:",
        validators=[DataRequired("You must have username"), Length(min=2, max=30)],
    )
    password = PasswordField(
        label="Password:", validators=[DataRequired(), Length(min=6)]
    )
    submit = SubmitField(label="Login")