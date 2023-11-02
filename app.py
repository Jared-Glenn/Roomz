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
    
    user = User.query.get_or_404(1)
    room = Room.query.get_or_404(room_id)
    
    # Get all teammates.
    teammate_list = (User_Room
                 .query
                 .filter(User_Room.room_id == room_id)
                 .limit(10)
                 .all())
    
    teammate_ids = []
    for teammate in teammate_list:
        teammate_ids.append(teammate.user_id)
    
    teammates = (User
                .query
                .filter(User.id.in_(teammate_ids))
                .all())
    
    events = Event.query.filter(Event.room==room.name)
    
    return render_template("room.html", user=user, room=room, teammates=teammates, events=events)


@app.route('/roomzie-demonstration')
def roomzie():
    """Shows a video of Roomzie's proposed functions."""
    
    return render_template("roomzie_demonstration.html")


@app.route('/in-development')
def in_dev():
    """Reserved for pages still in development."""
    
    return render_template("in_development.html")