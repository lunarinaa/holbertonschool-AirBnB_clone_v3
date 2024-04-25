#!/usr/bin/python3
"""amenities"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity).values()
    amenities_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    amenities = storage.all("Amenity").values()
    for amenity in amenities:
        if amenity.id == amenity_id:
            return jsonify(amenity.to_dict())
        else:
            abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Deletes a Amenity object:"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


# need to be revised
@app_views.route('/amenities', methods=['POST'])
@app_views.route('/amenities/', methods=['POST'])
def create_amenity():
    """Creates an Amenity"""
    try:
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
        if 'name' not in data:
            abort(400, 'Missing name')
        new_amenity = Amenity(name=data['name'])
        storage.new(new_amenity)
        storage.save()
        return jsonify(new_amenity.to_dict()), 201
    except Exception as e:
        if '404 Not Found' in str(e):
            return jsonify({'error': str(e)}), 404
        else:
            return jsonify({'error': str(e)}), 400


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Updates a Amenity object"""
    try:
        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)
        data = request.get_json()
        if not data:
            abort(400, 'Not a JSON')
        amenity.name = data.get('name', amenity.name)
        storage.save()
        return jsonify(amenity.to_dict()), 200
    except Exception as e:
        if '404 Not Found' in str(e):
            return jsonify({'error': str(e)}), 404
        else:
            return jsonify({'error': str(e)}), 400
