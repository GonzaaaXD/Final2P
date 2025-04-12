from flask import Blueprint, render_template, request, redirect, url_for, flash
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
    classification = request.form.get('classification')
    
    movie_service.add_movie(title, genre, year, classification)
    return redirect(url_for('movies.list_movies'))

@movie_bp.route('/delete/<int:movie_id>')
def delete_movie(movie_id):
    movie_service.delete_movie(movie_id)
    return redirect(url_for('movies.list_movies'))

@movie_bp.route('/update', methods=['PUT'])
def update_movie():
    movie_id = int(request.form.get('id'))
    title = request.form.get('titulo')
    genre = request.form.get('genre')
    year = int(request.form.get('year'))
    classification = request.form.get('classification')

    updated_movie = movie_service.update_movie(movie_id, title, genre, year, classification)

    if updated_movie:
        flash("Película actualizada exitosamente", "success")
    else:
        flash("Película no encontrada", "danger")

    return redirect(url_for('movies.list_movies'))