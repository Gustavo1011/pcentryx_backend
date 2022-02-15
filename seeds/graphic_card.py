"""
graphic_card.py: File to create data of GraphicCard
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.graphic_card import GraphicCard

class GraphicCardSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of GraphicCard"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/graphic_cards.json') as file:
                data = json.load(file)
                for graphic_card in data:
                    register_graphic_card = GraphicCard(
                        name=graphic_card['name'],
                        brand_component_id=graphic_card['brand_component_id']
                    )
                    db.session.add(register_graphic_card)
                db.session.commit()