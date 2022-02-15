"""
type_defective_component.py: File to define TypeDefectiveComponent Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('TypeDefectiveComponent')

class TypeDefectiveComponent(BaseDB, db.Model):
    """Defined class to TypeDefectiveComponent Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    name = ManageFieldsDB.db_string(180)
    image_url = ManageFieldsDB.db_text(nullable=True)
    min_amount = ManageFieldsDB.db_integer()
    max_amount = ManageFieldsDB.db_integer()
    type_computer_id = ManageFieldsDB.db_foreign_key('TypeComputer')

    type_computer = relator.has_one('TypeComputer')
    user_request_defective_components = relator.has_many('UserRequestDefectiveComponent')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "min_amount": self.min_amount,
            "max_amount": self.max_amount,
            "type_computer_id": self.type_computer_id,
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity