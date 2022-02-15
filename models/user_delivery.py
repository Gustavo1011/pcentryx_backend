"""
user_delivery.py: File to define UserDelivery Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('UserDelivery')

class UserDelivery(BaseDB, db.Model):
    """Defined class to UserDelivery Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    delivery_date = ManageFieldsDB.db_datetime()
    delivery_address = ManageFieldsDB.db_text()
    reference =  ManageFieldsDB.db_text(nullable=True)
    latitude = ManageFieldsDB.db_decimal(6,3,nullable=True)
    longitude = ManageFieldsDB.db_decimal(6, 3, nullable=True)
    instant_user_id = ManageFieldsDB.db_foreign_key('InstantUser')

    instant_user = relator.has_one('InstantUser')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "delivery_date": self.delivery_date,
            "delivery_address": self.delivery_address,
            "reference": self.reference,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "instant_user_id": self.instant_user_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity