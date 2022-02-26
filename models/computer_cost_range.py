"""
computer_cost_range.py: File to define ComputerCostRange Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('ComputerCostRange')

class ComputerCostRange(BaseDB, db.Model):
    """Defined class to ComputerCostRange Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    range_cost = ManageFieldsDB.db_string(180)

    cost_range_defective_components = relator.has_many('CostRangeDefectiveComponent')
    cost_services = relator.has_many('CostService')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "range_cost": self.range_cost,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity