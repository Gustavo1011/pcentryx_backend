"""
user.py: File to define User Model
"""
from app import db
from datetime import datetime
from flask_jwt_extended import get_jwt_identity
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB
from libraries.utils import get_local_isoformat
from pytz import timezone

relator = ManageRelationsDB('User')


class User(BaseDB, db.Model):  # pylint: disable=too-few-public-methods
    """Defined class to User Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    core_id = ManageFieldsDB.db_integer()
    name = ManageFieldsDB.db_string(50)
    lastname = ManageFieldsDB.db_string(50)
    username = ManageFieldsDB.db_string(50)
    password = ManageFieldsDB.db_string(255)
    email = ManageFieldsDB.db_string(50)
    avatar_url = ManageFieldsDB.db_text()
    is_enabled = ManageFieldsDB.db_boolean(default=True)

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "core_id": self.core_id,
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "avatar_url": self.avatar_url,
            "is_enabled": self.is_enabled,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }
        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)
        return entity

    def as_dict(self):
        """Return class description"""
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    def get_current_session(self):
        session = get_jwt_identity()
        return {
            'related_token_value': session.get('related_token_value'),
            'related_token_origin': session.get('related_token_origin'),
            'timezone': session.get('timezone'),
            'end_token': session.get('end_token')
        }

    def get_user(self):
        return {
            'id': self.id,
            'core_id': self.core_id,
            'name': self.name,
            'username': self.username,
            'lastname': self.lastname,
            'email': self.email,
            'avatar_url': self.avatar_url,
            'is_enabled': self.is_enabled
        }
    