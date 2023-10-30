"""User and Feedback models detailed."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to the database."""
    db.app = app
    db.init_app(app)
    

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
    rooms = db.relationship(
        "Room",
        secondary="users_rooms")
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        
    def __repr__(self):
        return f"<User {self.id} {self.username} {self.first_name} {self.last_name} {self.rooms} >"
 
 
 
class Room(db.Model):
    """Room model."""
    
    __tablename__ = "rooms"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                      nullable=False)
    notes = db.Column(db.String())
    users = db.relationship(
        "User",
        secondary="users_rooms")
    
    def __repr__(self):
        return f"<Department {self.id} {self.name} {self.notes} {self.users} >"



class User_Room(db.Model):
    """Many to many table for users and rooms."""
    
    __tablename__ = "users_rooms"
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        primary_key=True)
    room_id = db.Column(db.Integer,
                        db.ForeignKey('rooms.id'),
                        primary_key=True)