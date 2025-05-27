from flask import Flask

# App setup
app = Flask(__name__, template_folder='views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.secret_key = '!@#$%^&*()!@#$%^&*()!@#$%^&*()'

# Models
from models import db, seed
db.init_app(app)

# Controllers
from controllers.index import index
app.register_blueprint(index)
from controllers.hello_world_controller import hello_world
app.register_blueprint(hello_world)
from controllers.movie import movie
app.register_blueprint(movie)

# Run app
if __name__ == '__main__':
    print("Setting up...")

    with app.app_context():
        db.create_all()
        db.session.commit()
        seed()

    app.run(host='0.0.0.0')
