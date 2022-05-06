"""
user_pc_data.py: File to define UserPcData Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('UserPcData')

class UserPcData(BaseDB, db.Model):
    """Defined class to UserPcData Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    operating_system = ManageFieldsDB.db_string(180)
    ram_quantity = ManageFieldsDB.db_string(12)
    cpu_id = ManageFieldsDB.db_foreign_key('Cpu', nullable=True)
    cpu_request_name = ManageFieldsDB.db_string(180, nullable=True)
    dedicated_graphic_card = ManageFieldsDB.db_boolean(default=False)

    cpu = relator.has_one('Cpu')
    user_requests = relator.has_many('UserRequest')
    user_graphic_card_datas = relator.has_many('UserGraphicCardData')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "operating_system": self.operating_system,
            "ram_quantity": self.ram_quantity,
            "cpu_id": self.cpu_id,
            "dedicated_graphic_card": self.dedicated_graphic_card,
            "cpu_request_name": self.cpu_request_name,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity