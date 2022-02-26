"""
pc_specification.py: File to define PcSpecification Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('PcSpecification')

class PcSpecification(BaseDB, db.Model):
    """Defined class to PcSpecification Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    name = ManageFieldsDB.db_string(180)
    image_url = ManageFieldsDB.db_text(nullable=True)
    price = ManageFieldsDB.db_integer()
    ranking = ManageFieldsDB.db_decimal(2,1)
    cpu_name = ManageFieldsDB.db_string(180)
    gpu_name = ManageFieldsDB.db_string(180, nullable=True)
    ram_name = ManageFieldsDB.db_string(180)
    storage = ManageFieldsDB.db_string(180)
    case = ManageFieldsDB.db_string(180)
    psu_name = ManageFieldsDB.db_string(180)
    budget_pc_id = ManageFieldsDB.db_foreign_key('BudgetPc')

    budget_pc = relator.has_one('BudgetPc')
    pc_specification_programs = relator.has_many('PcSpecificationProgram')
    purchase_requests = relator.has_many('PurchaseRequest')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "price": self.price,
            "ranking": self.ranking,
            "cpu_name": self.cpu_name,
            "ram_name": self.ram_name,
            "storage": self.storage,
            "case": self.case,
            "gpu_name": self.gpu_name,
            "psu_name": self.psu_name,
            "budget_pc_id": self.budget_pc_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity