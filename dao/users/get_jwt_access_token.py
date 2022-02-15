"""
get_jwt_access_token.py: DAO file to get jwt access token.
"""
import time
import pytz
from flask import current_app
from flask_jwt_extended import create_access_token
from libraries.response import entity_response
from datetime import datetime
from pytz import timezone

class GetJWTAccessToken:  # pylint: disable=too-few-public-methods
    """Defined class to get jwt access token"""

    def __call__(self, result, timezone):
        if timezone.strip() not in pytz.all_timezones:
            return entity_response(400, message="Invalid timezone")
        now = int(time.time())
        jwt_time_token = current_app.config['JWT_ACCESS_TOKEN_EXPIRES']
        current_app.logger.info("GetJWTAccessToken: JWT_SECRET_KEY: " + \
            current_app.config['JWT_SECRET_KEY'])
        current_app.logger.info("GetJWTAccessToken: JWT_ACCESS_TOKEN_EXPIRES: " + \
            str(jwt_time_token))
        if jwt_time_token == "":
            return entity_response(400, message="Internal error. Please contact the administrator.")
        try:
            int(jwt_time_token)
        except ValueError:
            current_app.logger.info("Invalid JWT Time Token")
            return entity_response(400, message="Internal error. Please contact the administrator.")

        time_token = int(jwt_time_token)
        expire_in = now + time_token
        end_date = datetime.utcfromtimestamp(expire_in)
        end_token = end_date.isoformat(timespec='milliseconds')


        try:
            access_token = create_access_token(identity={
                **result.as_dict(),
                'timezone': timezone,
                'related_token_value': None,
                'related_token_origin': 'no_related_token',
                'end_token': end_token
            })
        except ValueError:
            current_app.logger.info("Could not create access token")
            return entity_response(400, message="Internal error. Please contact the administrator.")

        return {
            'user_id': result.id,
            'created_at': now,
            'expire_in': expire_in,
            'access_token': access_token
        }, 200
