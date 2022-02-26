"""
kit_mouse_keyboard.py: File to create data of KitMouseKeyboard
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.kit_mouse_keyboard import KitMouseKeyboard
from models.peripheral import Peripheral

class KitMouseKeyboardSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of KitMouseKeyboard"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/kit_mouse_keyboards.json') as file:
                data = json.load(file)
                for kit_mouse_keyboard in data:
                    register_kit_mouse_keyboard = Peripheral(
                        model_name=kit_mouse_keyboard['model_name'],
                        image_url=kit_mouse_keyboard['image_url'],
                        price=kit_mouse_keyboard['price'],
                        is_rgb=kit_mouse_keyboard['is_rgb'],
                        category_peripheral_id=kit_mouse_keyboard['category_peripheral_id']                    )
                    db.session.add(register_kit_mouse_keyboard)
                    db.session.commit()
                    attribute = kit_mouse_keyboard['attributes']
                    register_attributes = KitMouseKeyboard(
                        type_keyboard=attribute['type_keyboard'],
                        output_keyboard=attribute['output_keyboard'],
                        peripheral_id=register_kit_mouse_keyboard.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
