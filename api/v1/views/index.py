#!/usr/bin/python3
"""Defines the index page."""
from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


@app_views.route('/status')
def get_status():
    '''Gets the status of the API.
    '''
    return jsonify(status='OK')
