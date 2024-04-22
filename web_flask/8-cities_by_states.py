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


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Display a HTML page."""
    return render_template('8-cities_by_states.html', states=states, cts=cts)


@app.teardown_appcontext
def close_session(exception=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
