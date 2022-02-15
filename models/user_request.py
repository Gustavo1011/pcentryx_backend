"""
user_request.py: File to define UserRequest Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('UserRequest')

class UserRequest(BaseDB, db.Model):
    """Defined class to UserRequest Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    instant_user_id = ManageFieldsDB.db_foreign_key('InstantUser')
    service_id = ManageFieldsDB.db_foreign_key('Service')
    user_pc_data_id = ManageFieldsDB.db_foreign_key('UserPcData', nullable=True)
    user_laptop_data_id = ManageFieldsDB.db_foreign_key('UserLaptopData', nullable=True)

    instant_user = relator.has_one('InstantUser')
    service = relator.has_one('Service')
    user_pc_data = relator.has_one('UserPcData')
    user_laptop_data = relator.has_one('UserLaptopData')
    user_request_defective_components = relator.has_many('UserRequestDefectiveComponent')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "instant_user_id": self.instant_user_id,
            "service_id": self.service_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "user_pc_data_id": self.user_pc_data_id,
            "user_laptop_data_id": self.user_laptop_data_id,
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity