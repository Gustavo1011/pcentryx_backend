from flask_oauthlib.provider import OAuth2Provider
from flask import g
from datetime import datetime, timedelta

from models.oauth2 import OAuthClient
from models.oauth2 import OAuthGrant
from models.oauth2 import OAuthToken
from models.user import User

def create_oauth_provider(app, db):
    oauth = OAuth2Provider(app)

    @oauth.clientgetter
    def get_client(client_id):
        return OAuthClient.query.filter_by(client_id=client_id).first()

    @oauth.grantgetter
    def get_grant(client_id, code):
        return OAuthGrant.query.filter_by(client_id=client_id, code=code).first()

    @oauth.tokengetter
    def get_token(access_token=None, refresh_token=None):
        if access_token:
            return OAuthToken.query.filter_by(access_token=access_token).first()
        if refresh_token:
            return OAuthToken.query.filter_by(refresh_token=refresh_token).first()
        return None

    @oauth.grantsetter
    def set_grant(client_id, code, request, *args, **kwargs):
        expires = datetime.utcnow() + timedelta(seconds=100)
        grant = OAuthGrant(
            client_id=client_id,
            code=code['code'],
            redirect_uri=request.redirect_uri,
            scope=' '.join(request.scopes),
            user_id=g.user.id,
            expires=expires,
        )
        db.session.add(grant)
        db.session.commit()

    @oauth.tokensetter
    def set_token(token, request, *args, **kwargs):
        # In real project, a token is unique bound to user and client.
        # Which means, you don't need to create a token every time.
        tok = OAuthToken(**token)
        tok.user_id = request.user.id
        tok.client_id = request.client.client_id
        db.session.add(tok)
        db.session.commit()

    @oauth.usergetter
    def get_user(username, password, *args, **kwargs):
        # This is optional, if you don't need password credential
        # there is no need to implement this method
        return User.query.filter_by(username=username).first()

    return oauth