#!/usr/bin/python3
"""Create State objects that handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states/', methods=['GET'])
def get_states():
    """Retrieves a list of all State objects"""
    states = [state.to_dict() for state in storage.all("State").values()]
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieves a State object by its id"""
    states = storage.all("State").values()
    state_object = [object.to_dict() for object in states
                    if object.id == state_id]
    if state_object == []:
        abort(404)
    return jsonify(state_object[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object"""
    states = storage.all("State").values()
    state_object = [object.to_dict() for object in states
                    if object.id == state_id]
    if state_object == []:
        abort(404)
    state_object.remove(state_object[0])
    for obj in states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """Creates a a new State"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def updates_state(state_id):
    """Updates a State object"""
    states = storage.all("State").values()
    state_object = [object.to_dict() for object in states
                    if object.id == state_id]
    if state_object == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state_object[0]['name'] = request.json['name']
    for object in states:
        if object.id == state_id:
            object.name = request.json['name']
    storage.save()
    return jsonify(state_object[0]), 200