"""
monitor.py: File to create data of Monitor
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.monitor import Monitor
from models.peripheral import Peripheral

class MonitorSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Monitor"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/monitors.json') as file:
                data = json.load(file)
                for monitor in data:
                    register_monitor = Peripheral(
                        model_name=monitor['model_name'],
                        image_url=monitor['image_url'],
                        price=monitor['price'],
                        category_peripheral_id=monitor['category_peripheral_id']                    )
                    db.session.add(register_monitor)
                    db.session.commit()
                    attribute = monitor['attributes']
                    register_attributes = Monitor(
                        frequency=attribute['frequency'],
                        panel=attribute['panel'],
                        resolution=attribute['resolution'],
                        response_time=attribute['response_time'],
                        screen_size=attribute['screen_size'],
                        hdr=attribute['hdr'],
                        peripheral_id=register_monitor.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
