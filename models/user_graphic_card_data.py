"""
user_graphic_card_data.py: File to define UserGraphicCardData Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('UserGraphicCardData')

class UserGraphicCardData(BaseDB, db.Model):
    """Defined class to UserGraphicCardData Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    user_pc_data_id = ManageFieldsDB.db_foreign_key('UserPcData')
    vram_quantity = ManageFieldsDB.db_string(12)
    graphic_card_id = ManageFieldsDB.db_foreign_key('GraphicCard', nullable=True)
    gpu_request_name = ManageFieldsDB.db_string(180, nullable=True)

    graphic_card = relator.has_one('GraphicCard')
    user_pc_data = relator.has_one('UserPcData')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "user_pc_data_id": self.user_pc_data_id,
            "vram_quantity": self.vram_quantity,
            "graphic_card_id": self.gpu_id,
            "gpu_request_name": self.gpu_request_name,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity