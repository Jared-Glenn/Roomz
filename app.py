"""Routes for each page."""

from flask import Flask, request, render_template, redirect, jsonify, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_bcrypt import Bcrypt
from models import db, connect_db, User, Room, User_Room, Event, Task
# from forms import RegisterForm, LoginForm, FeedbackForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///roomz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
db.create_all()

# bcrypt = Bcrypt()


# Main page

@app.route('/')
def desk():
    """User desk space."""
    
    user = User.query.get_or_404(1)
    
    rooms = []
    for room in user.rooms:
        rooms.append(room.name)
    events = (Event
              .query
              .filter(Event.room.in_(rooms))
              .order_by(Event.datetime.desc())
              .limit(100)
              .all())
    
    return render_template("desk.html", user=user, events=events)

@app.route('/floorplan')
def floorplan():
    """User floorplan."""
    
    user = User.query.get_or_404(1)
    
    return render_template("floorplan.html", user=user)

@app.route('/roomz/<room_id>')
def room(room_id):
    """Room."""
    
    room = Room.query.get_or_404(room_id)
    
    return render_template("room.html", room=room)