"""
peripheral.py: File to define Peripheral Model
"""
from app import db
from libraries.utils import get_local_isoformat
from managers.class_utils.manage_db.base_db import BaseDB
from managers.class_utils.manage_db.manage_fields_db import ManageFieldsDB
from managers.class_utils.manage_db.manage_relations_db import ManageRelationsDB

relator = ManageRelationsDB('Peripheral')

class Peripheral(BaseDB, db.Model):
    """Defined class to Peripheral Model"""
    __tablename__ = relator.plural_name

    id = ManageFieldsDB.db_primary_key()
    model_name = ManageFieldsDB.db_string(180)
    image_url = ManageFieldsDB.db_text(nullable=True)
    price = ManageFieldsDB.db_integer()
    is_rgb = ManageFieldsDB.db_boolean(default=False, nullable=True)
    category_peripheral_id = ManageFieldsDB.db_foreign_key('CategoryPeripheral')

    category_peripheral = relator.has_one('CategoryPeripheral')
    purchase_request_peripherals = relator.has_many('PurchaseRequestPeripheral')
    accessories = relator.has_many('Accessory')
    kit_mouse_keyboards = relator.has_many('KitMouseKeyboard')
    psus = relator.has_many('Psu')
    cameras = relator.has_many('Camera')
    headsets = relator.has_many('Headset')
    mouses = relator.has_many('Mouse')
    keyboards = relator.has_many('Keyboard')
    monitors = relator.has_many('Monitor')
    speakers = relator.has_many('Speaker')

    def get_response(self, **kwargs):
        """Return response"""
        entity = {
            "id": self.id,
            "model_name": self.model_name,
            "image_url": self.image_url,
            "price": self.price,
            "is_rgb": self.is_rgb,
            "category_peripheral_id": self.category_peripheral_id,
            "created_at": self.created_at.isoformat(timespec='milliseconds'),
            "updated_at": self.updated_at and self.updated_at.isoformat(timespec='milliseconds'),
            "deleted": self.deleted
        }

        if kwargs.get('with_timezone', True):
            entity["created_at"] = get_local_isoformat(self.created_at)
            if self.updated_at:
                entity["updated_at"] = get_local_isoformat(self.updated_at)

        return entity