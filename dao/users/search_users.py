"""
search_users.py: DAO file to search users.
"""
from flask import jsonify
from models.user import User

class SearchUsers:  # pylint: disable=too-few-public-methods
    """Defined class to search users"""

    def __call__(self) -> list:

        result = User.query.filter(User.deleted == 'false').all()
        users = []
        for user in result:
            users.append({
                "username": user.username,
                "email": user.email
            })

        return jsonify(users), 200
