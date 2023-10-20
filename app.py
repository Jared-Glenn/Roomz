"""Routes for each page."""

from flask import Flask, request, render_template, redirect, jsonify, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
# from models import db, connect_db, User, Department
# from forms import RegisterForm, LoginForm, FeedbackForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hash-login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# connect_db(app)
# app.app_context().push()
# db.create_all()

# bcrypt = Bcrypt()


# Main page

@app.route('/')
def desk():
    """User desk space."""
    
    return render_template("desk.html")