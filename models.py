"""Models for adoption."""
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

default_time = datetime.now()

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     )
    specie = db.Column(db.String(50),
                     nullable=False,
                     )
    url = db.Column(db.Text,
                          default = DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer)
    
    notes = db.Column(db.Text)
    
    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)
    