"""
mouse.py: File to create data of Mouse
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.mouse import Mouse
from models.peripheral import Peripheral

class MouseSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Mouse"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/mouses.json') as file:
                data = json.load(file)
                for mouse in data:
                    register_mouse = Peripheral(
                        model_name=mouse['model_name'],
                        image_url=mouse['image_url'],
                        price=mouse['price'],
                        is_rgb=mouse['is_rgb'],
                        category_peripheral_id=mouse['category_peripheral_id']                    )
                    db.session.add(register_mouse)
                    db.session.commit()
                    attribute = mouse['attributes']
                    register_attributes = Mouse(
                        sensor=attribute['sensor'],
                        dpi=attribute['dpi'],
                        colour=attribute['colour'],
                        peripheral_id=register_mouse.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()