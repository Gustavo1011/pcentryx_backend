"""
type_computer.py: File to create data of TypeComputer
"""

from flask_seeder import Seeder
from models.type_computer import TypeComputer


class TypeComputerSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of TypeComputer"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        type_computers = [ 
            {"name": "PC"},
            {"name": "Laptop"}
        ]

        for type_computer in type_computers:
            data = TypeComputer(
                name = type_computer["name"]
            )
            self.db.session.add(data)
        self.db.session.commit()
