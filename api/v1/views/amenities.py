#!/usr/bin/python3
"""amenities"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity

# 3/25
@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """Retrieves the list of all Amenity objects"""
    amenity = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for unit in amenity])

# need to be revised
@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
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