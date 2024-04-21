#!/usr/bin/python3
"""
This module supplies a script that starts a flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays HBNB!
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays HBNB!
    """
    return f'C {escape(text)}'.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
