"""
billing_detail.py: File to define BillingDetail Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('BillingDetail')

class BillingDetail(BaseDB, db.Model):
    """Defined class to BillingDetail Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    address = ManageFieldsDB.db_text()
    email = ManageFieldsDB.db_string(128)
    phone_number = ManageFieldsDB.db_string(50)
    is_company = ManageFieldsDB.db_boolean(default=False)

    billing_detail_companies = relator.has_many('BillingDetailCompany')
    billing_detail_natural_persons = relator.has_many('BillingDetailNaturalPerson')
    purchase_requests = relator.has_many('PurchaseRequest')

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