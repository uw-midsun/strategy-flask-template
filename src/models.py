from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from . import db  # from __init__.py


class User(db.Model):
    # Custom table name in database
    __tablename__ = "users"

    # Auto Generated Fields:
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)

    # Data input by user:
    name = db.Column(db.String(100), nullable=False)
