#!/usr/bin/python3
"""plases"""

from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.city import City
from api.v1.views import app_views

@app_views.route('/cities/<city_id>/places', method=['GET'])
def get_place(city_id):
    """Retrieves the list of all Place objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = [place.to_dict() for place in city]
    return jsonify(places)