"""
type_service.py: File to create data of TypeService
"""

from flask_seeder import Seeder
from models.type_service import TypeService
from models.minimal_type_service import MinimalTypeService


class TypeServiceSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of TypeService"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        type_services = [ 
            {"name": "Reparación"},
            {"name": "Mantenimiento"},
            {"name": "Repotenciamiento"}
        ]

        for type_service in type_services:
            
            with_sub_services = ["Reparación", "Mantenimiento"]
            
            if type_service["name"] not in with_sub_services:
                data = TypeService(
                    name = type_service["name"]
                )
                self.db.session.add(data)
                self.db.session.commit()
                minimal_type_service_id = MinimalTypeService(
                    type_service_id = data.id
                )
                self.db.session.add(minimal_type_service_id)
            else:
                data = TypeService(
                    name = type_service["name"]
                )
                self.db.session.add(data)
        self.db.session.commit()

        