"""
login_user.py: DAO file to login.
"""
from flask import jsonify, current_app
from flask_babel import gettext
from models.user import User
from libraries.fernet import compare_password

class LoginUser:  # pylint: disable=too-few-public-methods
    """Defined class to login"""

    # pylint: disable=too-many-return-statements
    def __call__(self, request):
        if not current_app.config["JWT_SECRET_KEY"]:
            return jsonify({"msg": gettext("Login not available")}), 400

        if not request.is_json:
            return jsonify({"msg": gettext("Missing JSON in request")}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username:
            return jsonify({"msg": gettext("Missing username parameter")}), 400
        if not password:
            return jsonify({"msg": gettext("Missing password parameter")}), 400

        result = User.query.filter(
            User.username == username, User.deleted == "false"
        ).first()
        if result is None:
            return jsonify({"msg": gettext("Bad username")}), 400

        compare = compare_password(hash_password=result.password, password=password)

        if compare is False:
            return jsonify({"msg": gettext("Bad password")}), 400

        return result, 200
