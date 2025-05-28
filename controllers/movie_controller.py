from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

from models import db
from models.movie import Movie
from models.movie import MovieForm

movie_controller = Blueprint('movie_controller', __name__)

@movie_controller.route('/Movie', methods=['GET'])
def movie_index():
    movie_genre = request.args.get('MovieGenre', "", type=str)
    search_string = request.args.get('SearchString', "", type=str)

    movies = Movie.query.filter(
        (Movie.genre == movie_genre) if movie_genre != "" else True,
    ).filter(
        (Movie.title.contains(search_string)) if search_string != "" else True
    ).all()

    genres = [x[0] for x in Movie.query.with_entities(Movie.genre).distinct().all()]

    return render_template("movie/index.html", movies=movies, genres=genres, movie_genre=movie_genre, search_string=search_string)

@movie_controller.route('/Movie/Details/<int:ID>', methods=['GET'])
def movie_details(ID):
    movie = Movie.query.get_or_404(ID)

    return render_template("movie/details.html", movie=movie)

@movie_controller.route('/Movie/Delete/<int:ID>', methods=['GET'])
def movie_delete(ID):
    movie = Movie.query.get_or_404(ID)

    return render_template("movie/delete.html", movie=movie)

@movie_controller.route('/Movie/Delete/<int:ID>', methods=['POST'])
def movie_delete_post(ID):
    movie = Movie.query.get_or_404(ID)

    # Delete the movie
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('movie_controller.movie_index'))

@movie_controller.route('/Movie/Create', methods=['GET', 'POST'])
def movie_create():
    form = MovieForm()

    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            release_date=form.release_date.data,
            genre=form.genre.data,
            price=form.price.data,
            rating=form.rating.data
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('movie_controller.movie_index'))
    
    return render_template("movie/create.html", form=form)

@movie_controller.route('/Movie/Edit/<int:ID>', methods=['GET', 'POST'])
def movie_edit(ID):
    movie = Movie.query.get_or_404(ID)
    form = MovieForm(obj=movie)

    if form.validate_on_submit():
        form.populate_obj(movie)
        db.session.commit()
        return redirect(url_for('movie_controller.movie_index'))

    return render_template("movie/edit.html", form=form, movie=movie)
