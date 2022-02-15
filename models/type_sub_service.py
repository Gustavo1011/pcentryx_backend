"""
type_sub_service.py: File to define TypeSubService Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('TypeSubService')

class TypeSubService(BaseDB, db.Model):
    """Defined class to TypeSubService Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    name = ManageFieldsDB.db_string(180)
    image_url = ManageFieldsDB.db_text(nullable=True)
    type_service_id = ManageFieldsDB.db_foreign_key('TypeService')
    minimal_type_service_id = ManageFieldsDB.db_foreign_key('MinimalTypeService')
    

    type_service = relator.has_one('TypeService')
    minimal_type_service = relator.has_one('MinimalTypeService')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "type_service_id": self.type_service_id,
            "minimal_type_service_id": self.minimal_type_service_id,
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity