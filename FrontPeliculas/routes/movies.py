from flask import Blueprint, render_template, request, redirect, url_for
from services.movie_service import MovieService

movie_bp = Blueprint('movies', __name__, url_prefix='/movies')
movie_service = MovieService()

@movie_bp.route('/')
def list_movies():
    movies = movie_service.get_all_movies()
    return render_template('index.html', movies=movies)

@movie_bp.route('/add', methods=['POST'])
def add_movie():
    title = request.form.get('title')
    genre = request.form.get('genre')
    year = request.form.get('year')
    rating = request.form.get('rating')
    
    movie_service.add_movie(title, genre, year, rating)
    return redirect(url_for('movies.list_movies'))

@movie_bp.route('/delete/<int:movie_id>')
def delete_movie(movie_id):
    movie_service.delete_movie(movie_id)
    return redirect(url_for('movies.list_movies'))
