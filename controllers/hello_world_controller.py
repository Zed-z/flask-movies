from flask import Blueprint, render_template, request

hello_world_controller = Blueprint('hello_world_controller', __name__)

"""
@hello_world_controller.route('/HelloWorld', methods=['GET'])
def hello_world_controller_index():
    return "This is my default action..."
"""

@hello_world_controller.route('/HelloWorld', methods=['GET'])
def hello_world_controller_index():
    return render_template("hello_world/index.html")

@hello_world_controller.route('/HelloWorld/Welcome2', methods=['GET'])
def hello_world_controller_welcome2():
    name = request.args.get('name', 'World')
    numtimes = request.args.get('numtimes', 1, type=int)

    #return f"Hello {name}, NumTimes is: {numtimes}"
    return render_template("hello_world/welcome2.html", name=name, numtimes=numtimes)

@hello_world_controller.route('/HelloWorld/Welcome', methods=['GET'])
@hello_world_controller.route('/HelloWorld/Welcome/<int:ID>', methods=['GET'])
def hello_world_controller_welcome(ID=1):
    name = request.args.get('name', 'World')

    #return f"Hello {name}, ID: {ID}"
    return render_template("hello_world/welcome.html", name=name, ID=ID)

