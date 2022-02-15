"""
type_computer.py: File to create data of TypeComputer
"""

from flask_seeder import Seeder
from models.brand_component import BrandComponent


class BrandComponentSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of BrandComponent"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        brand_components = [ 
            {"name": "AMD"},
            {"name": "Intel"},
            {"name": "Nvidia"}
        ]

        for brand_component in brand_components:
            data = BrandComponent(
                name = brand_component["name"]
            )
            self.db.session.add(data)
        self.db.session.commit()
