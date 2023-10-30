"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Room, User_Room


db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/rooms.csv') as rooms:
    db.session.bulk_insert_mappings(Room, DictReader(rooms))

with open('generator/users_rooms.csv') as users_rooms:
    db.session.bulk_insert_mappings(User_Room, DictReader(users_rooms))

db.session.commit()