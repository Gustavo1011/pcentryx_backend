"""
speaker.py: File to create data of Speaker
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.speaker import Speaker
from models.peripheral import Peripheral

class SpeakerSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Speaker"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/speakers.json') as file:
                data = json.load(file)
                for speaker in data:
                    register_speaker = Peripheral(
                        model_name=speaker['model_name'],
                        image_url=speaker['image_url'],
                        price=speaker['price'],
                        category_peripheral_id=speaker['category_peripheral_id']                    )
                    db.session.add(register_speaker)
                    db.session.commit()
                    attribute = speaker['attributes']
                    register_attributes = Speaker(
                        subwoofer=attribute['subwoofer'],
                        satellite_speaker=attribute['satellite_speaker'],
                        peripheral_id=register_speaker.id
                    )
                    db.session.add(register_attributes)
                db.session.commit()
