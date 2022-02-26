"""
billing_detail_company.py: File to define BillingDetailCompany Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('BillingDetailCompany')

class BillingDetailCompany(BaseDB, db.Model):
    """Defined class to BillingDetailCompany Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    ruc = ManageFieldsDB.db_string(20)
    business_name = ManageFieldsDB.db_string(180)
    billing_detail_id = ManageFieldsDB.db_foreign_key('BillingDetail')

    billing_detail = relator.has_one('BillingDetail')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "address": self.address,
            "email": self.email,
            "phone_number": self.phone_number,
            "is_company": self.is_company,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity