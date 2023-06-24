from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    email = EmailField("Please enter your emaill address")
    password = PasswordField("Please enter your password")
    first_name = StringField("Please enter your first name")
    last_name = StringField("Please enter your last name")

    city = StringField("Please enter the city in which you live in")
    country = StringField("Please enter the country that you live in")

    allergies = BooleanField("Please select all of your allergies", choices=["milk/lactose", "eggs", "fish", "shellfish",
    "peanuts", "tree nuts", "wheat", "soy", "none of the above"])
    dietary_restrictions = BooleanField("Please select your dietary restrictions", choices=["gluten-free", "dairy-free", 
    "vegetarian", "vegan", "pescatarian", "nut-free", "shellfish-free", "sugar-free", "kosher", "halal"])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = EmailField("Please enter your emaill address")
    password = PasswordField("Please enter your password")
    submit = SubmitField()