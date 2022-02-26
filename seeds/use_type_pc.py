"""
use_type_pc.py: File to create data of UseTypePc
"""

from flask_seeder import Seeder
from models.use_type_pc import UseTypePc

class UseTypePcSeeder(Seeder): # pylint: disable=too-few-public-methods
    """Defined class to data of UseTypePc"""

    # pylint: disable=super-init-not-called
    def __init__(self, db):
        self.db = db

    def run(self):  # pylint: disable=too-many-locals
        use_type_pcs = [ 
            {"name": "Ofimática"},
            {"name": "Gaming/Streaming"},
            {"name": "Profesional"}
        ]

        for use_type_pc in use_type_pcs:
            data = UseTypePc(
                name = use_type_pc["name"]
            )
            self.db.session.add(data)
        self.db.session.commit()
