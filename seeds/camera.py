"""
camera.py: File to create data of Camera
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.camera import Camera
from models.peripheral import Peripheral

class CameraSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Camera"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/cameras.json') as file:
                data = json.load(file)
                for camera in data:
                    register_camera = Peripheral(
                        model_name=camera['model_name'],
                        image_url=camera['image_url'],
                        price=camera['price'],
                        category_peripheral_id=camera['category_peripheral_id']                    )
                    db.session.add(register_camera)
                    db.session.commit()
                    attribute = camera['attributes']
                    register_attributes = Camera(
                        resolution=attribute['resolution'],
                        output=attribute['output'],
                        peripheral_id=register_camera.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
