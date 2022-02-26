"""
mouse.py: File to define Mouse Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('Mouse')

class Mouse(BaseDB, db.Model):
    """Defined class to Mouse Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    sensor = ManageFieldsDB.db_string(100)
    dpi = ManageFieldsDB.db_string(50)
    colour = ManageFieldsDB.db_string(100, nullable=True)
    peripheral_id = ManageFieldsDB.db_foreign_key('Peripheral')

    peripheral = relator.has_one('Peripheral')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "sensor": self.sensor,
            "dpi": self.dpi,
            "colour": self.colour,
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