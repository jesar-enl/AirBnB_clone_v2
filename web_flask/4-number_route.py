#!/usr/bin/python3
"""
A script to display the `number` route
"""


from flask import Flask


# initialize the application using the variable `app`
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    '''This function returns a simple greeting'''
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """returns a single line"""
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c(text):
    '''
    this route returns the text given in the url
    '''
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'},
           methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python(text):
    '''
    Returns a python route with a default value
    if no text is passed
    '''
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''check if the text given in the url is a number'''
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
