#!/usr/bin/env python3
"""Start link class to table in database."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
states = storage.all(State)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page."""
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
