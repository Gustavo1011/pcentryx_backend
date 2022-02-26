"""
cost_range_defective_component.py: File to create data of CostRangeDefectiveComponent
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.cost_range_defective_component import CostRangeDefectiveComponent

class CostRangeDefectiveComponentSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of CostRangeDefectiveComponent"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/cost_range_defective_components.json') as file:
                data = json.load(file)
                for cost_range_defective_component in data:
                    register_cost_range_defective_component = CostRangeDefectiveComponent(
                        range_price_component=cost_range_defective_component['range_price_component'],
                        computer_cost_range_id=cost_range_defective_component['computer_cost_range_id'],
                        type_defective_component_id=cost_range_defective_component['type_defective_component_id']
                    )
                    db.session.add(register_cost_range_defective_component)
                db.session.commit()
