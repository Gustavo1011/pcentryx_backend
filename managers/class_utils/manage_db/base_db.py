"""
base_db.py: File to define Base Model
"""
from app import db
from libraries.utils import get_now
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB

class BaseDB:
    """Base Model"""
    created_at = ManageFieldsDB.db_datetime(default=get_now)
    updated_at = ManageFieldsDB.db_datetime(nullable=True, default=None)
    deleted = ManageFieldsDB.db_boolean()

    @classmethod
    def create(cls, data={}, attr_verifies=[str]):
        filter_verify = []
        for attr_verify in attr_verifies:
            filter_verify.append(
                getattr(cls, attr_verify) == data.get(attr_verify)
            )
        instance = cls.query.filter(
            *filter_verify
        ).first()
        if instance is not None:
            for key in data:
                setattr(instance, key, data[key])
        else:
            instance = cls(**data)
            db.session.add(instance)
        db.session.commit()
        return instance
