from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp

from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric(18, 2), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.String(5), nullable=False)

class MovieForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[
            DataRequired(message="Title is required."),
            Length(min=3, max=60, message="Title must be between 3 and 60 characters.")
        ]
    )
    release_date = DateField(
        'Release Date',
        validators=[DataRequired(message="Release date is required.")],
        format='%Y-%m-%d'
    )
    price = DecimalField(
        'Price',
        validators=[
            DataRequired(message="Price is required."),
            NumberRange(min=1, max=100, message="Price must be between 1 and 100.")
        ]
    )
    genre = StringField(
        'Genre',
        validators=[
            DataRequired(message="Genre is required."),
            Length(max=30, message="Genre must be at most 30 characters."),
            Regexp(r'^[A-Z]+[a-zA-Z\s]*$', message="Genre must start with a capital letter and contain only letters and spaces.")
        ]
    )
    rating = StringField(
        'Rating',
        validators=[
            DataRequired(message="Rating is required."),
            Length(max=5, message="Rating must be at most 5 characters."),
            Regexp(r'^[A-Z]+[a-zA-Z0-9"\'\s-]*$', message="Invalid rating format.")
        ]
    )
