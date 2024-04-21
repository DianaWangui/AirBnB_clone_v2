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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
def python_text(text):
    """
    Displays python and text with a default value
    """
    mytext = text.replace('_', ' ')
    return "Python %s" % escape(mytext)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays number n
    """
    return "%d is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
