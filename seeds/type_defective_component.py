"""
type_defective_component.py: File to create data of TypeDefectiveComponent
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.type_defective_component import TypeDefectiveComponent

class TypeDefectiveComponentSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of TypeDefectiveComponent"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/type_defective_components.json') as file:
                data = json.load(file)
                for type_defective_component in data:
                    register_type_defective_component = TypeDefectiveComponent(
                        name=type_defective_component['name'],
                        type_computer_id=type_defective_component['type_computer_id']
                    )
                    db.session.add(register_type_defective_component)
                db.session.commit()
