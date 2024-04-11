#!/usr/bin/python3
'''This script starts a Flask web application'''
from flask import Flask, render_template


app = Flask(__name__)
'''Creates a Flask application instance'''

@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Will display the following string when accessed'''
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Will display the following string when accessed'''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''Will display the following string when accessed. Receives a value in
    the text variable and replaces '_' with spaces'''
    return 'C ' + str(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is cool'):
    '''Will display the following string when accessed. Receives a value in
    the text variable and replaces '_' with spaces. If no value is written,
    it will use the default'''
    return 'Python ' + str(text.replace('_', ' '))

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    '''Will display the following string when accessed only if the value
    received is an integer'''
    if n.isdigit():
        return n + ' is a number'
    else:
        return 'Error: n must be an integer'
    
@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    '''Will display an HTML page when accessed only if the value received is
    an integer'''
    if n.isdigit():
        return render_template('5-number.html', value=int(n))
    else:
        return 'Error: n must be an integer'
    
@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    '''Will display an HTML page when accessed only if the value received is
    an integer and will state if that value is an even or odd number'''
    if isinstance(n, int):
        even_odd = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', value=n, parity=even_odd)
    else:
        return 'Error: n must be an integer'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)