#!/usr/bin/python3
"""Starting web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def display():
    """Display method"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """Display method"""
    state = storage.all(State).get(id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html')   
    


@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100)
