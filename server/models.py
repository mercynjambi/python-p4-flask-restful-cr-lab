from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)  # Name is required
    image = db.Column(db.String)  # Allow image to be null
    price = db.Column(db.Float)   # Allow price to be null

    def __repr__(self):
        return f'<Plant {self.name}>'
