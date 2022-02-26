"""
pc_specification.py: File to create data of PcSpecification
"""
import json
import os

from app import db
from models.pc_specification import PcSpecification
from models.pc_specification_program import PcSpecificationProgram

class PcSpecificationSeeder:  # pylint: disable=too-few-public-methods
    """Defined class to data of PcSpecification"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):
        """Run PcSpecification seeders"""
        app_setting = os.getenv('CREATE_SEED', 'deployment')
        if app_setting == 'deployment':
            with open('/app/seeds/json/pc_specifications.json') as file:
                data = json.load(file)
                for pc_specification in data:
                    register_pc_specification = PcSpecification(
                        name=pc_specification["name"],
                        image_url=pc_specification["image_url"],
                        price=pc_specification['price'],
                        ranking=pc_specification["ranking"],
                        cpu_name=pc_specification["cpu_name"],
                        gpu_name=pc_specification["gpu_name"],
                        ram_name=pc_specification["ram_name"],
                        storage=pc_specification["storage"],
                        case=pc_specification["case"],
                        psu_name=pc_specification["psu_name"],
                        budget_pc_id=pc_specification["budget_pc_id"]
                    )
                    db.session.add(register_pc_specification)
                    db.session.commit()
                    for pc_specification_program in pc_specification['pc_specification_programs']:
                        register_ideal_program = PcSpecificationProgram(
                            average_fps=pc_specification_program['average_fps'],
                            image_url=pc_specification_program['image_url'],
                            program_id=pc_specification_program['program_id'],
                            pc_specification_id=register_pc_specification.id
                        )
                        db.session.add(register_ideal_program)
                        db.session.commit()
