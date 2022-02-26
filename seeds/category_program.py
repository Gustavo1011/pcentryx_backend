"""
category_program.py: File to create data of CategoryProgram
"""

from flask_seeder import Seeder
from models.category_program import CategoryProgram

class CategoryProgramSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of CategoryProgram"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        category_programs = [ 
            {"name": "basico"},
            {"name": "modelado/arquitectura"},
            {"name": "programador"},
            {"name": "sonido"},
            {"name": "edicion"},
            {"name": "contable"},
            {"name": "streaming"},
            {"name": "gamer"},
            {"name": "videojuegos"}
        ]

        for category_program in category_programs:
            data = CategoryProgram(
                name = category_program["name"]
            )
            self.db.session.add(data)
        self.db.session.commit()