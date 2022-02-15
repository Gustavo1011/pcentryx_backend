"""
service.py: File to create data of Service
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.service import Service
from models.type_service import TypeService
from models.type_sub_service import TypeSubService
from models.minimal_type_service import MinimalTypeService

class ServiceSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Service"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/services.json') as file:
                data = json.load(file)
                for service in data:
                    type_service = TypeService.query.filter(
                        TypeService.name == service['type_service_name'],
                    ).first()
                    if service['type_sub_service_name'] is None:
                        minimal_type_service = MinimalTypeService.query.filter(
                            MinimalTypeService.type_service_id == type_service.id
                        ).first()
                        register_service = Service(
                            type_computer_id=service['type_computer_id'],
                            minimal_type_service_id=minimal_type_service.id,
                            amount=service['amount'],
                            description=service['description']
                        )
                        db.session.add(register_service)
                    else:
                        type_sub_service = TypeSubService.query.filter(
                            TypeSubService.name == service['type_sub_service_name'],
                        ).first()
                        register_service = Service(
                            type_computer_id=service['type_computer_id'],
                            minimal_type_service_id=type_sub_service.minimal_type_service.id,
                            amount=service['amount'],
                            description=service['description']
                        )
                        db.session.add(register_service)
                db.session.commit() 