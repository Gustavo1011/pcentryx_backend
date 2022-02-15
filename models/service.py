"""
service.py: File to define Services Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('Service')

class Service(BaseDB, db.Model):
    """Defined class to Service Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    amount = ManageFieldsDB.db_integer()
    type_computer_id = ManageFieldsDB.db_foreign_key('TypeComputer')
    minimal_type_service_id = ManageFieldsDB.db_foreign_key('MinimalTypeService')
    description = ManageFieldsDB.db_text(nullable=True)

    type_computer = relator.has_one('TypeComputer')
    minimal_type_service = relator.has_one('MinimalTypeService')
    user_requests = relator.has_many('UserRequest')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "amount": self.amount,
            "type_computer_id": self.type_computer_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "description": self.description,
            "minimal_type_service_id": self.minimal_type_service_id,
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity