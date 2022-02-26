"""
purchase_request.py: File to define PurchaseRequest Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('PurchaseRequest')

class PurchaseRequest(BaseDB, db.Model):
    """Defined class to PurchaseRequest Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    name = ManageFieldsDB.db_string(180)
    pc_specification_id = ManageFieldsDB.db_foreign_key('PcSpecification')
    billing_detail_id = ManageFieldsDB.db_foreign_key('BillingDetail')
    instant_user_id = ManageFieldsDB.db_foreign_key('InstantUser')

    billing_detail = relator.has_one('BillingDetail')
    pc_specification = relator.has_one('PcSpecification')
    instant_user = relator.has_one('InstantUser')
    purchase_request_peripherals = relator.has_many('PurchaseRequestPeripheral')
    purchase_request_programs = relator.has_many('PurchaseRequestProgram')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "name": self.name,
            "pc_specification_id": self.pc_specification_id,
            "billing_detail_id": self.billing_detail_id,
            "instant_user_id": self.instant_user_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity