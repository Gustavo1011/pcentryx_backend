"""
user_laptop_data.py: File to define UserLaptopData Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('UserLaptopData')

class UserLaptopData(BaseDB, db.Model):
    """Defined class to UserLaptopData Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    is_repaired = ManageFieldsDB.db_boolean(default=False)
    is_repowered = ManageFieldsDB.db_boolean(default=False)
    model_laptop_id = ManageFieldsDB.db_foreign_key('ModelLaptop')
    laptop_request_name = ManageFieldsDB.db_string(180, nullable=True)


    model_laptop = relator.has_one('ModelLaptop')
    user_requests = relator.has_many('UserRequest')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "is_repaired": self.is_repaired,
            "is_repowered": self.is_repowered,
            "model_laptop_id": self.model_laptop_id,
            "laptop_request_name": self.laptop_request_name,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity