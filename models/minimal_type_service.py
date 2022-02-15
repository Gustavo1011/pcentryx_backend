"""
minimal_type_service.py: File to define MinimalTypeService Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('MinimalTypeService')

class MinimalTypeService(BaseDB, db.Model):
    """Defined class to MinimalTypeService Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    type_service_id = ManageFieldsDB.db_foreign_key('TypeService')

    services = relator.has_many('Service')
    type_sub_services = relator.has_many('TypeSubService')
    type_service = relator.has_one('TypeService')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "type_service_id": self.type_service_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity