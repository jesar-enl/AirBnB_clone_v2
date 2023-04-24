#!/usr/bin/python3
# A script to create a route to the home displaying `Hello HBNB`

from flask import Flask


# initialize the application using the variable `app`
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    '''This function returns a simple greeting'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
