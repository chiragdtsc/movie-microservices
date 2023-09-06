from app import db
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    popularity = db.Column(db.Float, nullable=False)
    imdb_score = db.Column(db.Float, nullable=False)
    genre = db.Column(ARRAY(db.String(100)), nullable=False)
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