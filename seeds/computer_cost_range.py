"""
computer_cost_range.py: File to create data of ComputerCostRange
"""

from flask_seeder import Seeder
from models.computer_cost_range import ComputerCostRange

class ComputerCostRangeSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of ComputerCostRange"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        computer_cost_ranges = [ 
            {"range_cost": "1000 a 2500"},
            {"range_cost": "2500 a 4000"},
            {"range_cost": "4000 a 8000"},
            {"range_cost": "8000 a más"}
        ]

        for computer_cost_range in computer_cost_ranges:
            data = ComputerCostRange(
                range_cost = computer_cost_range["range_cost"]
            )
            self.db.session.add(data)
        self.db.session.commit()
