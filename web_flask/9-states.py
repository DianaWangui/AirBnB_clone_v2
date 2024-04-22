#!/usr/bin/python3
"""
This module supplies a script that starts a flask web application
"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
states = storage.all(State)
cts = storage.all(City)


@app.route('/states', strict_slashes=False)
def list_states():
    """Display a HTML page."""
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_state(id):
    """Display a HTML page."""
    return render_template('9-states.html', states=states, cts=cts, id=id)


@app.teardown_appcontext
def close_session(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
