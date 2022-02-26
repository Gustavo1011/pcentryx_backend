"""
keyboard.py: File to create data of Keyboard
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.keyboard import Keyboard
from models.peripheral import Peripheral

class KeyboardSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Keyboard"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/keyboards.json') as file:
                data = json.load(file)
                for keyboard in data:
                    register_keyboard = Peripheral(
                        model_name=keyboard['model_name'],
                        image_url=keyboard['image_url'],
                        price=keyboard['price'],
                        is_rgb=keyboard['is_rgb'],
                        category_peripheral_id=keyboard['category_peripheral_id']                    )
                    db.session.add(register_keyboard)
                    db.session.commit()
                    attribute = keyboard['attributes']
                    register_attributes = Keyboard(
                        type=attribute['type'],
                        switch=attribute['switch'],
                        output=attribute['output'],
                        peripheral_id=register_keyboard.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
