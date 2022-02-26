"""
cost_service.py: File to define CostService Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('CostService')

class CostService(BaseDB, db.Model):
    """Defined class to CostService Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    amount = ManageFieldsDB.db_string(10)
    computer_cost_range_id = ManageFieldsDB.db_foreign_key('ComputerCostRange')
    service_id = ManageFieldsDB.db_foreign_key('Service')

    computer_cost_range = relator.has_one('ComputerCostRange')
    service = relator.has_one('Service')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "computer_cost_range_id": self.computer_cost_range_id,
            "service_id": self.service_id,
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity