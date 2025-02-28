import enum
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from apps import db


# ========== ARTISTS DATA MODEL ==========
class ArtistsData(db.Model):
    __tablename__ = "artists_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)
