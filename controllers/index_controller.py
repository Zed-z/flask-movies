from flask import Blueprint, render_template

index_controller = Blueprint('index_controller', __name__)

@index_controller.route('/', methods=['GET'])
def root():
    return render_template("index.html")
