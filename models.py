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
    password = db.Column(db.String(),
                         nullable=False)
    email = db.Column(db.String(50),
                      unique=True,
                      nullable=False)
    first_name = db.Column(db.String(30),
                           nullable=False)
    last_name = db.Column(db.String(30),
                          nullable=False)
    department = db.Column(db.Integer,
                           db.ForeignKey('departments.id'))
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'department': self.department
        }
        
    def __repr__(self):
        return f"<User {self.id} {self.username} {self.password} {self.email} {self.first_name} {self.last_name} {self.department} >"
 
 
 
 class Department(db.Model):
    """Department model."""
    
    __tablename__ = "departments"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                      nullable=False)
    manager_id = db.Column(db.String(),
                        db.ForeignKey('users.id'))
    
    def __repr__(self):
        return f"<Department {self.id} {self.title} {self.content} {self.username} >"
