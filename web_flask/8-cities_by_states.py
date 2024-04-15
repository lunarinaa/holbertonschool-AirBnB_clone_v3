#!/usr/bin/python3
"""Starting web application"""
from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """Displays an HTML page"""
    states = sorted(storage.all("State").values(), key=lambda st: st.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
