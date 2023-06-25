# the database file must be wiped before using and then created again in the terminal!

from flask import Flask, render_template, session, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, DietaryRestrictionForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

# from populate_db import populate_food_items


app = Flask(__name__)

# used to protect against modifying cookies! MUST HAVE!
app.config['SECRET_KEY'] = "b272d0b5e8ddc9e3ff92e6853766147c"

# creates a new file of site.db for the database of users
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# creates URI for the food items database, need to bind db to SQLAlchemy instance
app.config['SQLALCHEMY_BINDS'] = {
    'food_db': 'sqlite:///food_items.db'
}

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=False)
    first_name = db.Column(db.String(20), unique=False)
    last_name = db.Column(db.String(20), unique=False)
    city = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)

    allergies = db.relationship('Allergy', backref="user", lazy=True)
    dietary_restrictions = db.relationship(
        'DietaryRestriction', backref="user", lazy=True)

    def __repr__(self):  # for testing
        return f"User('{self.email}', '{self.first_name}', '{self.last_name}', '{self.city}', '{self.country}', '{self.first_name}')"


class FoodItem(db.Model):
    # id jk necessary oy else there is no primary key column specified
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # more parameters?

    def __repr__(self):
        return f"FoodItem('{self.name}', '{self.description}')"


# create database file and tables
# db.create_all()
# with app.app_context():
#     db.create_all(bind_key='food_db')


class Allergy(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    allergy = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.Integer, db.ForeignKey(
        "user.email"), nullable=False)  # using email as foreign key

    def __repr__(self):
        return f"Allergy('{self.allergy}', '{self.user_email}')"


class DietaryRestriction(db.Model):
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    dietary_restriction = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.Integer, db.ForeignKey(
        "user.email"), nullable=False)  # using email as foreign key

    def __repr__(self):
        return f"DietaryRestriction('{self.dietary_restriction}', '{self.user_email}')"


# creates a new home page and functions underneath run on this page unless it encounters another route method
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        city = form.city.data
        country = form.country.data

        user = User(first_name=first_name, last_name=last_name,
                    email=email, password=password, city=city, country=country)
        session["user_email"] = user.email

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('allergy'))

    return render_template("register.html", form=form)


@app.route("/allergy", methods=['GET', 'POST'])
def allergy():

    # form = AllergyForm()
    user_email = session.get("user_email", None)

    # if form.validate_on_submit():
    #     for a in form.allergies.data:
    #         allergy = Allergy(allergy = a, user_email = user_email)
    #     return redirect(url_for('dietary-restriction'))

    if request.method == 'POST':
        selected_options = request.form.getlist('allergies')

        for a in selected_options:
            allergy = Allergy(allergy=a, user_email=user_email)
        return redirect(url_for('dietary-restriction'))

    return render_template("allergy.html")


@app.route("/dietary-restriction", methods=['GET', 'POST'])
def dietary_restriction():
    form = DietaryRestrictionForm()
    return render_template("dietary-restriction.html", form=form)


def create_tables():
    with app.app_context():
        db.create_all()


def populate_food_items():
    with app.app_context():
        # Create the food items
        pizza = FoodItem(name='Pizza', description='gluten')
        burger = FoodItem(name='Burger', description='gluten')
        salad = FoodItem(name='Salad', description='nuts')

        # Add the food items to the database
        db.session.add(pizza)
        db.session.add(burger)
        db.session.add(salad)

        # Commit the changes to the database
        db.session.commit()


if __name__ == '__main__':  # allows us to run the file using only "python filename.py"
    create_tables()
    populate_food_items()  # Call the function to populate the food items database
    app.run(debug=True)
