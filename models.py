"""User and Feedback models detailed."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

def connect_db(app):
    """Connect to the database."""
    db.app = app
    db.init_app(app)
    
    
class Pinned(db.Model):
    """Connetion of a pinner and the pinned person."""
    
    __tablename__='pinned'
    
    pinned_user = db.Column(db.Integer,
                            db.ForeignKey('users.id', ondelete='cascade'),
                            primary_key=True)
    pinning_user = db.Column(db.Integer,
                             db.ForeignKey('users.id', ondelete="cascade"),
                             primary_key=True)
    

class User(db.Model):
    """User model."""
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    username = db.Column(db.String(20),
                         unique=True,
                         nullable=False)
    first_name = db.Column(db.String(30),
                           nullable=False)
    last_name = db.Column(db.String(30),
                          nullable=False)
    job_title = db.Column(db.String(50))
    availability = db.Column(db.String(20))
    rooms = db.relationship(
        "Room",
        secondary="users_rooms",
        back_populates='users')
    pinned_people = db.relationship(
        "User",
        secondary="pinned",
        primaryjoin=(Pinned.pinned_user == id),
        secondaryjoin=(Pinned.pinning_user == id),
        backref=backref('pinning_user', lazy='dynamic'),
        lazy='dynamic'
    )
        
    def __repr__(self):
        return f"<User {self.id} {self.username} {self.first_name} {self.last_name} {self.job_title} {self.availability} {self.rooms} {self.pinned_people} >"
 
 
class Room(db.Model):
    """Room model."""
    
    __tablename__ = "rooms"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                      nullable=False,
                      unique=True)
    notes = db.Column(db.String())
    users = db.relationship(
        "User",
        secondary="users_rooms",
        back_populates='rooms')
    tasks = db.relationship('Task')
    events = db.relationship('Event')
    
    def __repr__(self):
        return f"<Room {self.id} {self.name} {self.notes} {self.users} {self.tasks} {self.events} >"


class Task(db.Model):
    """Task model."""
    
    __tablename__ = "tasks"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    complete = db.Column(db.String(5))
    item = db.Column(db.String(100),
                     nullable=False)
    room = db.Column(db.Integer,
                     db.ForeignKey('rooms.id', ondelete='CASCADE'),
                     nullable=False)
    
    def __repr__(self):
        return f"<Task {self.id} {self.complete} {self.item} {self.room} >"
    

class Event(db.Model):
    """Event model."""
    
    __tablename__ = "events"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    datetime = db.Column(db.DateTime,
                     nullable=False)
    room = db.Column(db.String(),
                     db.ForeignKey('rooms.name', ondelete='CASCADE'),
                     nullable=False)
    
    def __repr__(self):
        return f"<Event {self.id} {self.name} {self.datetime} {self.room} >"
    
    

class User_Room(db.Model):
    """Many to many table for users and rooms."""
    
    __tablename__ = "users_rooms"
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        primary_key=True)
    room_id = db.Column(db.Integer,
                        db.ForeignKey('rooms.id'),
                        primary_key=True)
    