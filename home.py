#the database file must be wiped before using and then created again in the terminal!

from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = "b272d0b5e8ddc9e3ff92e6853766147c" #used to protect against modifying cookies! MUST HAVE!
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" #creates a new file of site.db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Account table for database
class User(db.Model):
    email =  db.Column(db.String, primary_key = True, unique = True)
    password = db.Column(db.String(50), nullable=False, unique=False)
    first_name = db.Column(db.String(20), unique=False)
    last_name = db.Column(db.String(20), unique=False)
    city = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    allergies = db.relationship('Allergy', backref="user", lazy = True) #will be a list, links to Symptom class
    dietary_restrictions = db.relationship('DietaryRestriction', backref="user", lazy = True)

    def __repr__(self): #for testing
        return f"User('{self.email}', '{self.first_name}', '{self.last_name}', '{self.city}', '{self.country}', '{self.first_name}')"

#Symptom table for database
class Allergy(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique = True)
    allergy = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.Integer, db.ForeignKey("user.email"), nullable = False) #using email as foreign key

    def __repr__(self):
        return f"Allergy('{self.allergy}', '{self.user_email}')"

#Medical Conditions table for database
class DietaryRestriction(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique = True)
    dietary_restriction = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.Integer, db.ForeignKey("user.email"), nullable = False) #using email as foreign key

    def __repr__(self):
        return f"DietaryRestriction('{self.dietary_restriction}', '{self.user_email}')"


@app.route("/", methods=['GET','POST']) #creates a new home page and functions underneath run on this page unless it encounters another route method (i think)
@app.route("/home", methods=['GET','POST'])
def home():
    return render_template("home.html")

if __name__ == '__main__': #allows us to run the file using only "python filename.py"
    app.run(debug=True)
