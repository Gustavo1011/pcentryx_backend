"""
user_access.py: File to verify credentials and get session token
"""
from flask_babel import gettext
from interface import implements
from interfaces.users.user_access import IUserAccess
from dao.users.login_user import LoginUser
from dao.users.get_jwt_access_token import GetJWTAccessToken
from libraries.response import entity_response
# pylint: disable=too-few-public-methods, unpacking-non-sequence
class UserAccessProvider(implements(IUserAccess)):
    """Defined class to verify credentials and get session token"""
    def login(self, user, timezone):
        """Get user session"""
        login_user = LoginUser()
        result, code = login_user(user)
        if code == 400:
            return result, code
        if code == 200:
            result, code = GetJWTAccessToken()(result, timezone)
            if code == 400:
                return result, code
            return entity_response(
                code,
                message=gettext("Access token generated successfully"),
                result=result
            )
        return False
