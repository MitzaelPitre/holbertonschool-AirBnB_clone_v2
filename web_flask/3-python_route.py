#!/usr/bin/python3
"""
Flask module that starts a web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Route that displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Route that displays 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Route that displays 'C' followed by the value of the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ A route that displays python and input text """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port='5000'
    )
