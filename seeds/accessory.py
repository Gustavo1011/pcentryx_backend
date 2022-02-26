"""
accsessory.py: File to create data of Accessory
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.accessory import Accessory
from models.peripheral import Peripheral

class AccessorySeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Accessory"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/accessories.json') as file:
                data = json.load(file)
                for accsessory in data:
                    register_accsessory = Peripheral(
                        model_name=accsessory['model_name'],
                        image_url=accsessory['image_url'],
                        price=accsessory['price'],
                        category_peripheral_id=accsessory['category_peripheral_id']                    )
                    db.session.add(register_accsessory)
                    db.session.commit()
                    register_attributes = Accessory(
                        attributes=accsessory['attributes'],
                        peripheral_id=register_accsessory.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()