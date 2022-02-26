"""
billing_detail_natural_person.py: File to define BillingDetailNaturalPerson Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('BillingDetailNaturalPerson')

class BillingDetailNaturalPerson(BaseDB, db.Model):
    """Defined class to BillingDetailNaturalPerson Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    dni = ManageFieldsDB.db_string(15)
    name = ManageFieldsDB.db_string(180)
    billing_detail_id = ManageFieldsDB.db_foreign_key('BillingDetail')

    billing_detail = relator.has_one('BillingDetail')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "dni": self.dni,
            "name": self.name,
            "billing_detail_id": self.billing_detail_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity