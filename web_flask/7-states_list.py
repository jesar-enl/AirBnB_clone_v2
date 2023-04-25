#!/usr/bin/python3
"""Start a web app on `0.0.0.0:5000` and fetch data from
DBStorage to load all Cities by states"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Close the session with DB"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """Display the list of states in a web page"""
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
