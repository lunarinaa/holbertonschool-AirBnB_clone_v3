#!/usr/bin/python3
"""cities"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State

@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """Retrieves the list of all City objects"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieves a City object."""
    all_cities = storage.all(City).values()
    the_city = [city.to_dict() for city in all_cities if city.id == city_id]
    if the_city == []:
        abort(404)
    return jsonify(the_city[0])

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Deletes a City object"""
    the_city = storage.get(City, city_id)
    if the_city is None:
        abort(404)
    storage.delete(the_city)
    storage.save()
    return jsonify({}), 200

# need to be revised
@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Creates a City"""
    data = request.get_json()
    the_state = storage.get(State, state_id)
    if not data:
        abort(400, 'Not a JSON')
    if the_state is None:
        abort(404)
    if 'name' not in data:
        abort(400, 'Missing name')
    new_city = City(name=data['name'], state_id=state_id)
    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201

@app_views.route('cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Updates a City object"""
    data = request.get_json()
    the_city = storage.get("City", city_id)
    if not data:
        abort(400, 'Not a JSON')
    if the_city is None:
        abort(404)
    the_city.name = data.get('name', the_city.name)
    storage.save()
    return jsonify(the_city.to_dict()), 200