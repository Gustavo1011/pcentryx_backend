"""
delete_user.py: DAO file to delete specific user.
"""
from flask import jsonify
from flask_babel import gettext
from models.user import User
from app import db

class DeleteUser:  # pylint: disable=too-few-public-methods
    """Defined class to delete specific user"""

    def __call__(self, user_id):
        user = User.query.filter(User.id == user_id, User.deleted == "false").first()
        if user is None:
            return jsonify({"msg": gettext("The record was not found")}), 400

        user.deleted = True
        # db.session.delete(user)
        db.session.commit()

        return jsonify({"msg": gettext("The record has been deleted successfully")}), 200
