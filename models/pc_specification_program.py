"""
pc_specification_program.py: File to define PcSpecificationProgram Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('PcSpecificationProgram')

class PcSpecificationProgram(BaseDB, db.Model):
    """Defined class to PcSpecificationProgram Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    average_fps = ManageFieldsDB.db_string(12, nullable=True)
    image_url = ManageFieldsDB.db_text(nullable=True)
    program_id = ManageFieldsDB.db_foreign_key('Program')
    pc_specification_id = ManageFieldsDB.db_foreign_key('PcSpecification')

    program = relator.has_one('Program')
    pc_specification = relator.has_one('PcSpecification')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "average_fps": self.average_fps,
            "image_url": self.image_url,
            "program_id": self.program_id,
            "pc_specification_id": self.pc_specification_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity