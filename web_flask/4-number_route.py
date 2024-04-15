#!/usr/bin/python3
"""
Flask module that returns a Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ A route that displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A route that displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ A route that displays C and input text """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ A route that displays Python followed by the value of the text variable """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ A route that displays input number only if an int is input """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
