from app import db
from models.movies import Movie

class MovieRepository:
    @staticmethod
    def create_movie(movie_data: dict):
        """Create a new movie record in the database."""
        new_movie = Movie(name=movie_data['name'], director=movie_data['director'], popularity=movie_data['popularity'], imdb_score=movie_data['imdb_score'], genre=movie_data['genre'])
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.serialize()

    @staticmethod
    def get_movie_by_id(movie_id):
        """Retrieve a movie record from the database by ID."""
        return Movie.query.get(movie_id).serialize()

    @staticmethod
    def filter_movies(name):
        """Retrieve a movie record from the database by ID."""
        movies = Movie.query.filter_by(name=movie_name).all()
        return [movie.serialize() for movie in movies]

    @staticmethod
    def get_all_movies():
        """Retrieve all movie records from the database."""
        movies = Movie.query.all()
        return [movie.serialize() for movie in movies]

    @staticmethod
    def update_movie(movie_id, movie_updated_data):
        """Update a movie record in the database by ID."""
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = movie_updated_data['name']
            movie.genre = movie_updated_data['genre']
            movie.popularity = movie_updated_data['popularity']
            movie.imdb_score = movie_updated_data['imdb_score']
            movie.director = movie_updated_data['director']
            db.session.add(movie)
            db.session.commit()
        return movie.serialize()

    @staticmethod
    def delete_movie(movie_id):
        """Delete a movie record from the database by ID."""
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
        return movie
