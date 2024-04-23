#!/usr/bin/python3
"""Index"""


from api.v1.views import app_views
from flask import jsonify
from models import storage
import models

classes = {"amenities": "Amenity", "cities": "City",
           "places": "Place", "reviews": "Review",
           "states": "State",  "users": "User"}


@app_views.route('/status')
def status():
    """returns a JSON"""
    return jsonify({"status":  "OK"})


@app_views.route('/stats')
def stats():
    """Retrieves the number of each object by type"""
    counts = {}
    for cls in classes:
        counts[cls] = storage.count(classes[cls])
    return jsonify(counts)