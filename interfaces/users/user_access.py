"""
user_access.py: Interface to access with a user
"""
from interface import Interface

class IUserAccess(Interface):
    """Control User access"""

    def login(self, user, timezone):
        """Valid and return a valid access token"""
