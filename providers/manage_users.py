"""
manage_users.py: File to manage users
"""
from interface import implements
from interfaces.users.manage_users import IManageUsers

from dao.users.search_users import SearchUsers
from dao.users.store_user import StoreUser
from dao.users.get_user import GetUser
from dao.users.update_user import UpdateUser
from dao.users.delete_user import DeleteUser

class ManageUsersProvider(implements(IManageUsers)):
    """Defined class to manage users"""

    def search(self) -> list:
        """Return a list of filtered users"""
        search_users = SearchUsers()
        return search_users()

    def store(self, user):
        """Create a new user"""
        store_user = StoreUser()
        return store_user(user)

    def get(self, user_id):
        """Get information of a user"""
        get_user = GetUser()
        return get_user(user_id)

    def update(self, user_id, user):
        """Update a specific user"""
        update_user = UpdateUser()
        return update_user(user_id, user)

    def delete(self, user_id):
        """Delete a specific user"""
        delete_user = DeleteUser()
        return delete_user(user_id)
