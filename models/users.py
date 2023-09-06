from app import db
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'director': self.director,
            'popularity': self.popularity,
            'imdb_score': self.imdb_score,
        }