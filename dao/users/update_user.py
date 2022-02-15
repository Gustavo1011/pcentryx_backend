"""
update_user.py: DAO file to update user.
"""
from datetime import datetime
from flask import jsonify
from flask_babel import gettext
from models.user import User
from app import db
from libraries.fernet import generate_password

class UpdateUser:  # pylint: disable=too-few-public-methods
    """Defined class to update user"""

    def __call__(self, user_id, request):
        user = User.query.filter(User.id == user_id, User.deleted == "false").first()
        if user is None:
            return jsonify({"msg": gettext("The record was not found")}), 400

        valid_username = User.query.filter(
            User.username == request["username"],
            User.deleted == "false", User.id != user_id
        ).first()
        if valid_username is not None:
            return jsonify({"msg": gettext("The username already exists")}), 400

        valid_email = User.query.filter(
            User.email == request["email"],
            User.deleted == "false", User.id != user_id
        ).first()
        if valid_email is not None:
            return jsonify({"msg": gettext("The username already exists")}), 400

        user.username = request['username']
        user.email = request['email']
        user.updated_at = datetime.utcnow()

        if "password" in request:
            password = generate_password(request["password"])
            user.password = password

        db.session.commit()

        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        }), 200
