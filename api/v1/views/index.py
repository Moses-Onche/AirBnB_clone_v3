#!/usr/bin/python3
"""Defines the index page."""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """Get status of API."""
    return jsonify(status='OK')


@app.route('/stats')
def get_num_objects():
    """Get number of objects by type."""
    obj = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }

    for key, item in obj.items():
        obj[key] = storage.count(item)
    return jsonify(obj)
