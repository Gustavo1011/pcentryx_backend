"""
cpu.py: File to create data of Cpu
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.cpu import Cpu

class CpuSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Cpu"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/cpus.json') as file:
                data = json.load(file)
                for cpu in data:
                    register_cpu = Cpu(
                        name=cpu['name'],
                        brand_component_id=cpu['brand_component_id']
                    )
                    db.session.add(register_cpu)
                db.session.commit()