"""
oauth.py: File to create fake data of OAuth
"""
from datetime import datetime, timedelta
from flask_seeder import Seeder
from models.oauth2 import OAuthClient
from models.oauth2 import OAuthGrant
from models.oauth2 import OAuthToken

class OauthSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to Fake data of OAuth"""

    def run(self):
        client1 = OAuthClient(
            name='dev', client_id='dev', client_secret='dev',
            _redirect_uris=(
                'http://localhost:5000/user_management/authorized '
                'http://localhost/user_management/authorized'
            ),
        )

        client2 = OAuthClient(
            name='confidential', client_id='confidential',
            client_secret='confidential', client_type='confidential',
            _redirect_uris=(
                'http://localhost:5000/user_management/authorized '
                'http://localhost/user_management/authorized'
            ),
        )

        temp_grant = OAuthGrant(
            user_id=1, client_id='confidential',
            code='12345', scope='email',
            expires=datetime.utcnow() + timedelta(seconds=100)
        )

        access_token = OAuthToken(
            user_id=1, client_id='dev', access_token='expired', expires_in=0
        )

        access_token2 = OAuthToken(
            user_id=1, client_id='dev', access_token='never_expire'
        )

        try:
            self.db.session.add(client1)
            self.db.session.add(client2)
            self.db.session.add(temp_grant)
            self.db.session.add(access_token)
            self.db.session.add(access_token2)
            self.db.session.commit()
        except: # pylint: disable=bare-except
            self.db.session.rollback()
