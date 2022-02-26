"""
program.py: File to create data of Program
"""
import json
import os

from flask_seeder import Seeder

from app import db
from models.program import Program

class ProgramSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of Program"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/programs.json') as file:
                data = json.load(file)
                for program in data:
                    register_program = Program(
                        name=program['name'],
                        category_program_id=program['category_program_id'],
                        description=program['description']
                    )
                    db.session.add(register_program)
                db.session.commit()
