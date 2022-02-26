"""
program.py: File to define Program Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('Program')

class Program(BaseDB, db.Model):
    """Defined class to Program Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    name = ManageFieldsDB.db_string(180)
    description = ManageFieldsDB.db_text(nullable=True)
    category_program_id = ManageFieldsDB.db_foreign_key('CategoryProgram')

    category_program = relator.has_one('CategoryProgram')
    purchase_request_programs = relator.has_many('PurchaseRequestProgram')
    pc_specification_programs = relator.has_many('PcSpecificationProgram')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category_program_id": self.category_program_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity