import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth

MOVIE_PER_PAGE = 10
ACTOR_PER_PAGE = 20

# A function that will paginate the movies
def paginate_movies(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * MOVIE_PER_PAGE
    end = start + MOVIE_PER_PAGE

    movies = [movie.format() for movie in selection]
    current_movies = movies[start:end]

    return current_movies

# A function that will paginate the actors
def paginate_actors(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * ACTOR_PER_PAGE
    end = start + ACTOR_PER_PAGE

    actors = [actor.format() for actor in selection]
    current_actors = actors[start:end]

    return current_actors


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  #Allow '*' for origins.
  CORS(app, resources={r"*": {"origins": "*"}})

  # CORS headers
  @app.after_request
  def after_request(response):
    response.headers.add(
      'Access-Control-Allow-Headers',
      'Content-Type, Authorization, true')
    response.headers.add(
      'Access-Control-Allow-Methods',
      'GET, POST, PUT, PATCH, DELETE, OPTIONS')
    return response

  # =============== Endpoints =================

  # MAIN Route
  @app.route('/')
  def index():
    return render_template('index.html')

  # ============== Movies ====================

  # GET movies
  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies():

    # get all movies ordered by ID
    selection = Movie.query.order_by(Movie.id).all()

    # format the selection
    formatted_movies = paginate_movies(request, selection)

    # if there's no movies selected
    if len(formatted_movies) == 0:
      abort(404)

    return jsonify({
      'movies': formatted_movies,
      'total_movies': len(Movie.query.all()),
    })

  # POST movies
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def post_movies():

    # get the request body
    body = request.get_json()

    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)

    # if either one of them is empty, abort(400) ['bad request'-> 400]
    if new_title is None or new_release_date is None:
      abort(400)

    # initialize the new object
    new_movie = None

    try:
      # creating a new instance of Movie
      new_movie = Movie(title=new_title, release_date=new_release_date)

      new_movie.insert()

    except:
      abort(422)

    # get all movies ordered by ID
    selection = Movie.query.order_by(Movie.id).all()

    # format the selection
    formatted_movies = paginate_movies(request, selection)

    # if there's no movies selected
    if len(formatted_movies) == 0:
      abort(404)


    return jsonify({
      'id': new_movie.id,
      'movies': formatted_movies,
      'total_movies': len(Movie.query.all()),
    })

  # DELETE movies
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(movie_id):

    # get the movie with the given ID
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

    # if there's no movies selected
    if movie is None:
      abort(404)

    try:
      movie.delete()

    except:
      abort(422)


    return jsonify({
      'deleted': movie_id,
      'success': True,
    })

  # PATCH movies
  @app.route('/movies', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movies():

    # get the request content
    body = request.get_json()
    new_id = body.get('id', None)
    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)

    if new_id is None:
      abort(400)
    
    movie = Movie.query.filter(Movie.id == new_id).one_or_none()

    if movie is None:
      abort(404)

    # if one of the attributes changed, we will 
    # update it's corresponding attributes in the object
    if new_title is not None:
      movie.title = new_title
    if new_release_date is not None:
      movie.release_date = new_release_date

    try:
      movie.update()

    except:
      abort(422)

    return jsonify({
      'updated_movie': movie.format(),
      'success': True,
    })

  # ================ Actors =====================

  # GET actors
  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors():

    # get all movies ordered by ID
    selection = Actor.query.order_by(Actor.id).all()

    # format the selection
    formatted_actors = paginate_actors(request, selection)

    # if there's no actors selected
    if len(formatted_actors) == 0:
      abort(404)

    return jsonify({
      'actors': formatted_actors,
      'total_actors': len(Actor.query.all()),
    })

  # POST actors
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def post_actors():

    # get the request body
    body = request.get_json()

    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)

    # if either one of them is empty, abort(400) ['bad request'-> 400]
    if new_name is None or new_age is None or new_gender is None:
      abort(400)

    # initialize the new object
    new_actor = None

    try:
      # creating a new instance of Actor
      new_actor = Actor(name=new_name, age=new_age, gender=new_gender)

      new_actor.insert()

    except:
      abort(422)

    # get all actors ordered by ID
    selection = Actor.query.order_by(Actor.id).all()

    # format the selection
    formatted_actors = paginate_actors(request, selection)

    # if there's no actors selected
    if len(formatted_actors) == 0:
      abort(404)


    return jsonify({
      'id': new_actor.id,
      'name': new_actor.name,
      'actors': formatted_actors,
      'total_actors': len(Actor.query.all()),
    })

  # DELETE actors
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(actor_id):

    # get the actor with the given ID
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

    # if there's no actors selected
    if actor is None:
      abort(404)

    try:
      actor.delete()

    except:
      abort(422)


    return jsonify({
      'deleted': actor_id,
      'success': True,
    })

  # PATCH actors
  @app.route('/actors', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actors():

    # get the request content
    body = request.get_json()
    new_id = body.get('id', None)
    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)

    if new_id is None:
      abort(400)
    
    actor = Actor.query.filter(Actor.id == new_id).one_or_none()

    if actor is None:
      abort(404)

    # if one of the attributes changed, we will 
    # update it's corresponding attributes in the object
    if new_name is not None:
      actor.name = new_name
    if new_age is not None:
      actor.age = new_age
    if new_gender is not None:
      actor.gender = new_gender

    try:
      actor.update()

    except:
      abort(422)

    return jsonify({
      'updated_actor': actor.format(),
      'success': True,
    })

  """
    ErrorHandlers 
  """
  @app.errorhandler(404)
  def not_found(error):

        return jsonify({
            'success': False,
            'message': "resource not found",
            'error': 404
        }), 404

  @app.errorhandler(422)
  def unprocessable(error):

    return jsonify({
        'success': False,
        'message': "unprocessable",
        'error': 422,
    }), 422

  @app.errorhandler(405)
  def method_not_allowed(error):

    return jsonify({
        'success': False,
        'message': "method not allowed",
        'error': 405,
    }), 405

  @app.errorhandler(400)
  def bad_request(error):

    return jsonify({
        'success': False,
        'message': "bad request",
        'error': 400,
    }), 400

  @app.errorhandler(500)
  def internal_server_error(error):

    return jsonify({
        'success': False,
        'message': "internal server error",
        'error': 500,
    }), 500

  @app.errorhandler(AuthError)
  def auth_error(AuthError):

    return jsonify({
        'success': False,
        'error' : AuthError.error,
        'description': AuthError.error,
        'status_code': AuthError.status_code,
    })

  return app


app = create_app()


# run the app using "python3 {nameOfTheFile}.py"
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)