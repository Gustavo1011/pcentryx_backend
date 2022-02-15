"""
user_request_defective_component.py: File to define UserRequestDefectiveComponent Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('UserRequestDefectiveComponent')

class UserRequestDefectiveComponent(BaseDB, db.Model):
    """Defined class to UserRequestDefectiveComponent Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    user_request_id = ManageFieldsDB.db_foreign_key('UserRequest')
    type_defective_component_id = ManageFieldsDB.db_foreign_key('TypeDefectiveComponent')

    user_request = relator.has_one('UserRequest')
    type_defective_component = relator.has_one('TypeDefectiveComponent')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "user_request_id": self.user_request_id,
            "type_defective_component_id": self.type_defective_component_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity