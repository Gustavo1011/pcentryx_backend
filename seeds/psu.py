"""
psu.py: File to create data of Psu
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.psu import Psu
from models.peripheral import Peripheral

class PsuSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Psu"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/psus.json') as file:
                data = json.load(file)
                for psu in data:
                    register_psu = Peripheral(
                        model_name=psu['model_name'],
                        image_url=psu['image_url'],
                        price=psu['price'],
                        category_peripheral_id=psu['category_peripheral_id']                    )
                    db.session.add(register_psu)
                    db.session.commit()
                    attribute = psu['attributes']
                    register_attributes = Psu(
                        power=attribute['power'],
                        peripheral_id=register_psu.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
