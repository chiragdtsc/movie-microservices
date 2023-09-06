from flask_restx import Model, fields

MoviePayload = Model('MoviePayload', {
    'name': fields.String(required=True),
    'director': fields.String(required=False),
    'popularity': fields.Float(required=False),
    'imdb_score': fields.Float(required=False),
    'genre': fields.List(fields.String),
})