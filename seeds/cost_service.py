"""
cost_service.py: File to create data of CostService
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.cost_service import CostService

class CostServiceSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of CostService"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/cost_services.json') as file:
                data = json.load(file)
                for cost_service in data:
                    register_cost_service = CostService(
                        amount=cost_service['amount'],
                        computer_cost_range_id=cost_service['computer_cost_range_id'],
                        service_id=cost_service['service_id']
                    )
                    db.session.add(register_cost_service)
                db.session.commit()
