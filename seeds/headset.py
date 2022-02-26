"""
headset.py: File to create data of Headset
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.headset import Headset
from models.peripheral import Peripheral

class HeadsetSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Headset"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/headsets.json') as file:
                data = json.load(file)
                for headset in data:
                    register_headset = Peripheral(
                        model_name=headset['model_name'],
                        image_url=headset['image_url'],
                        price=headset['price'],
                        is_rgb=headset['is_rgb'],
                        category_peripheral_id=headset['category_peripheral_id']                    )
                    db.session.add(register_headset)
                    db.session.commit()
                    attribute = headset['attributes']
                    register_attributes = Headset(
                        sound=attribute['sound'],
                        microphone=attribute['microphone'],
                        output=attribute['output'],
                        peripheral_id=register_headset.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
