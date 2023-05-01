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


@app_views.route('/status', methods=['GET'])
def get_status():
    """Get status of API."""
    return jsonify(status='OK')


@app_views.route('/stats', methods=['GET'])
def get_num_objects():
    """Get number of objects by type."""
    count = {}
    objs = {
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User)
    }

    return jsonify(objs)
