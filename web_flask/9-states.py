#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def display():
    states = storage.all(State)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>')
def display(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=states)
    return render_template('9-states.html')




@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5100)
