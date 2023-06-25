from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    confirm_email = EmailField("Confirm Email Address", validators=[DataRequired(), Email(), EqualTo('email')])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')]);

    city = StringField("City")
    country = StringField("Country")

    submit = SubmitField("Next")

class LoginForm(FlaskForm):
    email = EmailField("Please enter your emaill address")
    password = PasswordField("Please enter your password")
    submit = SubmitField()