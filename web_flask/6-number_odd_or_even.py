#!/usr/bin/python3
"""
A script to display the `number` route
"""


from flask import Flask, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''return a template'''
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        return abort(404)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    '''display a HTML page only if n is an integer'''
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
