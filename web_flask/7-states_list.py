#!/usr/bin/python3
'''This script starts a Flask web application'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
'''Creates a Flask application instance '''

@app.route('/states_list', strict_slashes=False)
def states():
    return render_template('7-states_list.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)