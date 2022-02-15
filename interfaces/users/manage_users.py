"""
manage_users.py: Interface to manage users
"""
from interface import Interface

class IManageUsers(Interface):
    """Manage user access accounts"""

    def search(self):
        """Returns a list of users"""

    def store(self, user):
        """Store a user"""

    def get(self, user_id):
        """Get a user by ID"""

    def update(self, user_id, user):
        """Update a user by ID"""

    def delete(self, user_id):
        """Delete a user by ID"""
