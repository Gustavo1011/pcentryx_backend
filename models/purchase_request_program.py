"""
purchase_request_program.py: File to define PurchaseRequestProgram Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('PurchaseRequestProgram')

class PurchaseRequestProgram(BaseDB, db.Model):
    """Defined class to PurchaseRequestProgram Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    purchase_request_id = ManageFieldsDB.db_foreign_key('PurchaseRequest')
    program_id = ManageFieldsDB.db_foreign_key('Program')

    program = relator.has_one('Program')
    purchase_request = relator.has_one('PurchaseRequest')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "purchase_request_id": self.purchase_request_id,
            "program_id": self.program_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity