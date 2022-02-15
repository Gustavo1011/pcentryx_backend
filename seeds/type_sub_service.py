"""
type_sub_service.py: File to create data of type_sub_services
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.type_service import TypeService
from models.minimal_type_service import MinimalTypeService
from models.type_sub_service import TypeSubService

class TypeSubServiceSeeder(Seeder):
    """Defined class to data of TypeSubServiceSeeder"""
    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/type_sub_services.json') as file:
                data = json.load(file)
                for minimal_type_service in data:
                    type_service = TypeService.query.filter(
                        TypeService.name == minimal_type_service['type_service_name'],
                    ).first()

                    register_minimal_type_service = MinimalTypeService(
                        type_service_id=type_service.id
                    )
                    db.session.add(register_minimal_type_service)
                    db.session.commit()

                    type_sub_service = minimal_type_service['type_sub_service']
                    register_type_sub_service = TypeSubService(
                        name=type_sub_service['name'],
                        type_service_id=type_service.id,
                        minimal_type_service_id=register_minimal_type_service.id
                    )
                    db.session.add(register_type_sub_service)
                db.session.commit() 
