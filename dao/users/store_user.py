"""
store_user.py: DAO file to create user.
"""
from datetime import datetime
from flask import jsonify
from flask_babel import gettext
from models.user import User
from libraries.fernet import generate_password
from app import db

class StoreUser:  # pylint: disable=too-few-public-methods
    """Defined class to create user"""

    def __call__(self, user):
        valid_username = User.query.filter(
            User.username == user["username"], User.deleted == "false"
        ).first()
        if valid_username is not None:
            return jsonify({"msg": gettext("The username already exists")}), 400

        valid_email = User.query.filter(
            User.email == user["email"], User.deleted == "false"
        ).first()
        if valid_email is not None:
            return jsonify({"msg": gettext("The username already exists")}), 400

        password = generate_password(user["password"])
        created_at = datetime.utcnow()

        user = User(
            username=user["username"], password=password, email=user["email"],
            created_at=created_at, deleted=False
        )

        db.session.add(user)
        db.session.commit()

        return jsonify(user.as_dict()), 200
