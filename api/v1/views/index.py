#!/usr/bin/python3
"""Defines the index page."""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """Get status of API."""
    return jsonify(status='OK')
