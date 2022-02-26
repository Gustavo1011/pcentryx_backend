"""
category_peripheral.py: File to create data of CategoryPeripheral
"""

from flask_seeder import Seeder
from models.category_peripheral import CategoryPeripheral

class CategoryPeripheralSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of CategoryPeripheral"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        category_peripherals = [ 
            {"name": "Accesorio"},
            {"name": "Audífono"},
            {"name": "Cámara"},
            {"name": "Kit"},
            {"name": "Monitor"},
            {"name": "Mouse"},
            {"name": "Parlante"},
            {"name": "PSU"},
            {"name": "Teclado"}
        ]

        for category_peripheral in category_peripherals:
            data = CategoryPeripheral(
                name = category_peripheral["name"]
            )
            self.db.session.add(data)
        self.db.session.commit()