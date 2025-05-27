from flask_sqlalchemy import SQLAlchemy
from datetime import date
db = SQLAlchemy()

from .movie import Movie

def seed():
	if Movie.query.count() == 0:
		db.session.add_all([
			Movie(title="When Harry Met Sally", release_date=date(1989, 2, 12), genre="Romantic Comedy", price=7.99, rating="R"),
			Movie(title="Ghostbusters", release_date=date(1984, 3, 13), genre="Comedy", price=8.99, rating="G"),
			Movie(title="Ghostbusters 2", release_date=date(1986, 2, 23), genre="Comedy", price=9.99, rating="G"),
			Movie(title="Rio Bravo", release_date=date(1959, 4, 15), genre="Western", price=3.99, rating="NA"),
		])
		db.session.commit()
		print("Database seeded.")