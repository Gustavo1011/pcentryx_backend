"""
get_user.py: DAO file to get information from a specific user.
"""
from flask import jsonify
from flask_babel import gettext
from models.user import User

class GetUser:  # pylint: disable=too-few-public-methods
    """Defined class to get information from a specific user"""

    def __call__(self, user_id):
        user = User.query.filter(User.id == user_id, User.deleted == "false").first()
        if user is None:
            return jsonify({"msg": gettext("The record was not found")}), 400

        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }), 200
