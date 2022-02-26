"""
accessory.py: File to define Accessory Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('Accessory')

class Accessory(BaseDB, db.Model):
    """Defined class to Accessory Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    attributes = ManageFieldsDB.db_text()
    peripheral_id = ManageFieldsDB.db_foreign_key('Peripheral')

    peripheral = relator.has_one('Peripheral')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "attributes": self.attributes,
            "peripheral_id": self.peripheral_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity