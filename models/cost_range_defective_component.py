"""
cost_range_defective_component.py: File to define CostRangeDefectiveComponent Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('CostRangeDefectiveComponent')

class CostRangeDefectiveComponent(BaseDB, db.Model):
    """Defined class to CostRangeDefectiveComponent Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    range_price_component = ManageFieldsDB.db_string(180)
    computer_cost_range_id = ManageFieldsDB.db_foreign_key('ComputerCostRange')
    type_defective_component_id = ManageFieldsDB.db_foreign_key('TypeDefectiveComponent')

    computer_cost_range = relator.has_one('ComputerCostRange')
    type_defective_component = relator.has_one('TypeDefectiveComponent')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "range_price_component": self.range_price_component,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "computer_cost_range_id": self.computer_cost_range_id,
            "type_defective_component_id": self.type_defective_component_id,
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity