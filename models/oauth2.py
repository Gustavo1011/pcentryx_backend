"""
oauth2.py: File to define OAuthClient, OAuthGrant, OAuthToken Models
"""
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from app import db

from models.user import User

class OAuthClient(db.Model):  # pylint: disable=too-few-public-methods
    """Defined class to OAuthClient Model"""
    __tablename__ = 'oauth_clients'

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), comment="OAuth Client Name")
    client_id = db.Column(db.String(40), primary_key=True, comment="OAuth Client ID")
    client_secret = db.Column(
        db.String(55), nullable=False, comment="OAuth Client Secret"
    )
    client_type = db.Column(db.String(20), server_default='public', comment="OAuth Client Type")
    _redirect_uris = db.Column(db.Text, comment="OAuth Client Redirect URI")
    default_scope = db.Column(
        db.Text, server_default='email address',
        comment="OAuth Client Default Scope"
    )

    @property
    def user(self):
        """Return the first user"""
        return User.query.get(1)

    @property
    def redirect_uris(self):
        """Return the redirect uris"""
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        """Return the first redirect uri"""
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        """Return the default scope"""
        if self.default_scope:
            return self.default_scope.split()
        return []

    @property
    def allowed_grant_types(self):
        """Return the allowed grant types"""
        return ['authorization_code', 'password', 'client_credentials',
                'refresh_token']


class OAuthGrant(db.Model):  # pylint: disable=too-few-public-methods
    """Defined class to OAuthGrant Model"""
    __tablename__ = 'oauth_grants'

    id = db.Column(db.Integer, primary_key=True, comment="OAuth Grant ID")
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),
        comment="User ID"
    )
    user = relationship('User')
    client_id = db.Column(
        db.String(40), db.ForeignKey('oauth_clients.client_id', ondelete='CASCADE'),
        nullable=False, comment="OAuth Client ID"
    )
    client = relationship('OAuthClient')
    code = db.Column(
        db.String(255), nullable=False,
        comment="OAuth Grant Code"
    )
    redirect_uri = db.Column(db.String(255), comment="OAuth Grant Redirect URI")
    scope = db.Column(db.Text, comment="OAuth Grant Scope")
    expires = db.Column(db.DateTime, comment="OAuth Grant Expire Time")

    def delete(self):
        """Delete the OAuthGrant"""
        db.session.delete(self)
        db.session.commit()
        return self

    @property
    def scopes(self):
        """Return the scope"""
        if self.scope:
            return self.scope.split()
        return None


class OAuthToken(db.Model):  # pylint: disable=too-few-public-methods
    """Defined class to OAuthToken Model"""
    __tablename__ = 'oauth_tokens'

    id = db.Column(db.Integer, primary_key=True, comment="OAuth Token ID")
    client_id = db.Column(
        db.String(40), db.ForeignKey('oauth_clients.client_id', ondelete='CASCADE'),
        nullable=False, comment="OAuth Client ID"
    )
    client = relationship('OAuthClient')
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),
        comment="User ID"
    )
    user = relationship('User')
    token_type = db.Column(db.String(40), comment="OAuth Token Type")
    access_token = db.Column(db.String(255), comment="OAuth Access Token")
    refresh_token = db.Column(db.String(255), comment="OAuth Refresh Token")
    expires = db.Column(db.DateTime, comment="OAuth Token Expire Time")
    scope = db.Column(db.Text, comment="OAuth Token Scope")

    def __init__(self, **kwargs):
        expires_in = kwargs.pop('expires_in', None)
        if expires_in is not None:
            self.expires = datetime.utcnow() + timedelta(seconds=expires_in)

        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def scopes(self):
        """Return the scope"""
        if self.scope:
            return self.scope.split()
        return []

    def delete(self):
        """Delete the OAuthToken"""
        db.session.delete(self)
        db.session.commit()
        return self
