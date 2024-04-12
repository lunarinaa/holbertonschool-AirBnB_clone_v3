#!/usr/bin/python3
from flask import Flask
"""Starting a Flask web application"""

app = Flask(__name__)
"""object of Flask class"""


@app.route('/', strict_slashes=False)
def display():
    """method to display hello """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
