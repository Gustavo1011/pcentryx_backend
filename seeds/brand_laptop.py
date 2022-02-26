"""
brand_laptop.py: File to create data of BrandLaptop
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.brand_laptop import BrandLaptop

class BrandLaptopSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of BrandLaptop"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/brand_laptops.json') as file:
                data = json.load(file)
                for brand_laptop in data:
                    register_brand_laptop = BrandLaptop(
                        name=brand_laptop['name']
                    )
                    db.session.add(register_brand_laptop)
                db.session.commit()