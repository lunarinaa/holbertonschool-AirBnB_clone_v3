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
# @app_views.route('/amenities/<amenity_id>', methods=['GET'])
# def get_amenity(amenity_id):
#     """Retrieves a Amenity object"""
#     amenity = storage.get(Amenity, amenity_id)
#     if amenity is None:
#         abort(404)
#     return jsonify(amenity.to_dict())

# @app_views.route('/amenities/<amenity_id>', methods=['GET'])
# def get_amenity(amenity_id):
#      """Retrieves a Amenity object"""
#      amenities = storage.all("Amenity").values()
#      for amenity in amenities:
#          if amenity.id == amenity_id:
#              return jsonify(amenity.to_dict())
#          else:
#              abort(404)
#      return jsonify(amenity.to_dict())

@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    '''Retrieves an Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity_obj = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_obj == []:
        abort(404)
    return jsonify(amenity_obj[0])


             


# need to be revised
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
def create_amenity():
    """Creates an Amenity"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    new_amenity = Amenity(name=data['name'])
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Updates a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    amenity.name = data.get('name', amenity.name)
    storage.save()
    return jsonify(amenity.to_dict()), 200