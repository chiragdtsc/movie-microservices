from flask import request, jsonify
from flask_restx import Api, Resource, fields
from app import app, db
from payloads.movies import MoviePayload
from repositories.movie import MovieRepository

movies_api = Api(app, version='1.0', title='Movies CRUD API',
    description='A simple Movie management API',
)

# Define a namespace
movies_ns = movies_api.namespace('movies', description='Movie operations')

@movies_ns.route('/movie/<int:movie_id>')
class MovieResource(Resource):
    @movies_ns.marshal_with(MoviePayload)
    def get(self, movie_id):
        """Get a movie by ID"""
        movie = MovieRepository.get_movie_by_id(movie_id)
        if not movie:
            movies_ns.abort(404, message='Movie not found')
        return movie

    @movies_ns.expect(MoviePayload)
    @movies_ns.marshal_with(MoviePayload)
    def post(self):
        """Create a movie record"""
        movie = MovieRepository.create_movie(request.json)
        return movie

    @movies_ns.expect(MoviePayload)
    @movies_ns.marshal_with(MoviePayload)
    def put(self, movie_id):
        """Update a movie by ID"""
        movie = MovieRepository.get_movie_by_id(movie_id)
        if not movie:
            movies_ns.abort(404, message='Movie not found')

        data = request.json
        movie = MovieRepository.update_movie(movie_id, data)
        return movie

    @movies_ns.response(204, 'Movie deleted successfully')
    def delete(self, movie_id):
        """Delete a movie by ID"""
        movie = MovieRepository.get_movie_by_id(movie_id)
        if not movie:
            movies_ns.abort(404, message='Movie not found')
        return '', 204

@movies_ns.route('/filter')
class MoviesFilterResource(Resource):
    @movies_ns.marshal_list_with(MoviePayload)
    def get(self):
        """Filter movies based on various criteria."""
        name = request.args.get('name')
        popularity = request.args.get('popularity')
        imdb_score = request.args.get('imdb_score')
        director = request.args.get('director')
        genre = request.args.get('genre')

        query = Movie.query

        if name:
            query = query.filter(Movie.title.contains(name))

        if popularity:
            query = query.filter(Movie.popularity == float(popularity))

        if imdb_score:
            query = query.filter(Movie.imdb_score == float(imdb_score))

        if director:
            query = query.join(Movie.director).filter(Director.name == director)

        filtered_movies = query.all()
        return filtered_movies