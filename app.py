from flask import Flask

# App setup
app = Flask(__name__, template_folder='views')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.secret_key = '!@#$%^&*()!@#$%^&*()!@#$%^&*()'

# Models
from models import db, seed
db.init_app(app)

# Controllers
from controllers.index_controller import index_controller
app.register_blueprint(index_controller)
from controllers.hello_world_controller import hello_world_controller
app.register_blueprint(hello_world_controller)
from controllers.movie_controller import movie_controller
app.register_blueprint(movie_controller)

# Run app
if __name__ == '__main__':
    print("Setting up...")

    with app.app_context():
        db.create_all()
        db.session.commit()
        seed()

    app.run(host='0.0.0.0')
