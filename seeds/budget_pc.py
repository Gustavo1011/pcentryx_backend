"""
budget_pc.py: File to create data of BudgetPc
"""

from flask_seeder import Seeder
from models.budget_pc import BudgetPc

class BudgetPcSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of BudgetPc"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        budget_pcs = [ 
            {
                "name": "Básico",
                "use_type_pc_id": 1
            },
           {
                "name": "Medio",
                "use_type_pc_id": 1
            },
           {
                "name": "Alto",
                "use_type_pc_id": 1
            },
           {
                "name": "Básico",
                "use_type_pc_id": 2
            },
           {
                "name": "Medio",
                "use_type_pc_id": 2
            },
           {
                "name": "Alto",
                "use_type_pc_id": 2
            },
           {
                "name": "Básico",
                "use_type_pc_id": 3
            },
           {
                "name": "Medio",
                "use_type_pc_id": 3
            },
           {
                "name": "Alto",
                "use_type_pc_id": 3
            }
        ]

        for budget_pc in budget_pcs:
            data = BudgetPc(
                name = budget_pc["name"],
                use_type_pc_id = budget_pc["use_type_pc_id"]
            )
            self.db.session.add(data)
        self.db.session.commit()