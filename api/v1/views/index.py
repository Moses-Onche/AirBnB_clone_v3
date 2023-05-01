#!/usr/bin/python3
"""Defines the index page."""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.user import User


@app_views.route('/status')
def get_status():
    """Get status of API."""
    return jsonify(status='OK')


@app_views.route('/stats')
def get_num_objects():
    """Get number of objects by type."""
    count = {}
    obj = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }

    for key, item in obj.items():
        count[key] = storage.count(item)
    return jsonify(count)
