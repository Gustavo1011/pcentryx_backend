"""
model_laptop.py: File to create data of ModelLaptop
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.model_laptop import ModelLaptop

class ModelLaptopSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of ModelLaptop"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/model_laptop.json') as file:
                data = json.load(file)
                for model_laptop in data:
                    register_model_laptop = ModelLaptop(
                        name=model_laptop['name'],
                        brand_laptop_id=model_laptop['brand_laptop_id']
                    )
                    db.session.add(register_model_laptop)
                db.session.commit()