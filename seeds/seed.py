"""
seed.py: File to create all fake data
"""
import os
import datetime
from libraries.utils import snake_case
from seeds.service import ServiceSeeder
from seeds.type_computer import TypeComputerSeeder
from seeds.type_service import TypeServiceSeeder
from seeds.type_sub_service import TypeSubServiceSeeder
from seeds.type_defective_component import TypeDefectiveComponentSeeder
from seeds.brand_component import BrandComponentSeeder
from seeds.brand_laptop import BrandLaptopSeeder
from seeds.cpu import CpuSeeder
from seeds.model_laptop import ModelLaptopSeeder
from seeds.graphic_card import GraphicCardSeeder
from seeds.oauth import OauthSeeder
from seeds.accessory import AccessorySeeder
from seeds.budget_pc import BudgetPcSeeder
from seeds.camera import CameraSeeder
from seeds.category_peripheral import CategoryPeripheralSeeder
from seeds.category_program import CategoryProgramSeeder
from seeds.computer_cost_range import ComputerCostRangeSeeder
from seeds.cost_range_defective_component import CostRangeDefectiveComponentSeeder
from seeds.cost_service import CostServiceSeeder
from seeds.headset import HeadsetSeeder
from seeds.keyboard import KeyboardSeeder
from seeds.kit_mouse_keyboard import KitMouseKeyboardSeeder
from seeds.monitor import MonitorSeeder
from seeds.mouse import MouseSeeder
from seeds.pc_specification import PcSpecificationSeeder
from seeds.program import ProgramSeeder
from seeds.psu import PsuSeeder
from seeds.speaker import SpeakerSeeder
from seeds.use_type_pc import UseTypePcSeeder

class DatabaseSeed: # pylint: disable=too-few-public-methods
    """Defined class to create Data Fake"""

    # pylint: disable=invalid-name, line-too-long
    def __init__(self, db):
        self.SEED_TEST = os.getenv('SEED_TEST', "True") == 'True'
        self.db = db
        self.seeds = []

    def run(self):
        """Defined method to run Data Fake"""
        self.seeds = self.get_part_1()
        print('CREATE_SEED = {}'.format(os.getenv('CREATE_SEED', 'local')))
        print('SEED_TEST = {}'.format(os.getenv('SEED_TEST')))
        for row in self.seeds:
            print(str(datetime.datetime.now()) + " Running Seeder " + row["name"])
            if row["required"] or self.SEED_TEST:
                row["seed"].run()

    def run_part(self, number_part):
        """Run specific part"""
        if number_part == 1:
            self.seeds = self.get_part_1()
        self.run()

    def get_part_1(self):
        """Get part 1"""
        return [
            # CORE
            # DUDAS
            {"name": "OAuth", "seed": OauthSeeder(self.db), "required": True},
            {"name": "UseTypePc", "seed": UseTypePcSeeder(self.db), "required": True},
            {"name": "BudgetPc", "seed": BudgetPcSeeder(self.db), "required": True},
            {"name": "CategoryProgram", "seed": CategoryProgramSeeder(self.db), "required": True},
            {"name": "CategoryPeripheral", "seed": CategoryPeripheralSeeder(self.db), "required": True},
            {"name": "ComputerCostRange", "seed": ComputerCostRangeSeeder(self.db), "required": True},
            {"name": "TypeComputer", "seed": TypeComputerSeeder(self.db), "required": True},
            {"name": "TypeService", "seed": TypeServiceSeeder(self.db), "required": True},
            {"name": "TypeSubService", "seed": TypeSubServiceSeeder(self.db), "required": True},
            {"name": "BrandComponent", "seed": BrandComponentSeeder(self.db), "required": True},
            {"name": "BrandLaptop", "seed": BrandLaptopSeeder(self.db), "required": True},
            {"name": "Cpu", "seed": CpuSeeder(self.db), "required": False},
            {"name": "graphic_card", "seed": GraphicCardSeeder(self.db), "required": False},
            {"name": "ModelLaptop", "seed": ModelLaptopSeeder(self.db), "required": False},
            {"name": "TypeDefectiveComponent", "seed": TypeDefectiveComponentSeeder(self.db), "required": True},
            {"name": "Service", "seed": ServiceSeeder(self.db), "required": True},
            {"name": "CostRangeDefectiveComponent", "seed": CostRangeDefectiveComponentSeeder(self.db), "required": False},
            {"name": "CostService", "seed": CostServiceSeeder(self.db), "required": True},
            {"name": "Accessory", "seed": AccessorySeeder(self.db), "required": True},
            {"name": "Camera", "seed": CameraSeeder(self.db), "required": True},
            {"name": "Headset", "seed": HeadsetSeeder(self.db), "required": True},
            {"name": "Keyboard", "seed": KeyboardSeeder(self.db), "required": True},
            {"name": "KitMouseKeyboard", "seed": KitMouseKeyboardSeeder(self.db), "required": True},
            {"name": "Monitor", "seed": MonitorSeeder(self.db), "required": True},
            {"name": "Mouse", "seed": MouseSeeder(self.db), "required": True},
            {"name": "Program", "seed": ProgramSeeder(self.db), "required": True},
            {"name": "Psu", "seed": PsuSeeder(self.db), "required": True},
            {"name": "PcSpecification", "seed": PcSpecificationSeeder(self.db), "required": True},
            # ESTÁTICAS
            # ERP
        ]      
class UnitSeed:  # pylint: disable=too-few-public-methods
    """Defined class to create Data Fake"""

    # pylint: disable=invalid-name, line-too-long
    def __init__(self, db, name):
        self.SEED_TEST = os.getenv('SEED_TEST', "True") == 'True'
        self.db = db
        file = snake_case(name)
        class_name = name + 'Seeder'
        entity_module = __import__('seeds.%s' % file, fromlist=[class_name])
        instance = getattr(entity_module, class_name)
        self.seeds = [
            {"name": name, "seed": instance(db), "required": True}
        ]

    def run(self):
        """Defined method to run Data Fake"""
        print('CREATE_SEED = {}'.format(os.getenv('CREATE_SEED', 'local')))
        for row in self.seeds:
            print(str(datetime.datetime.now()) + " Running Seeder " + row["name"])
            if row["required"] or self.SEED_TEST:
                row["seed"].run()
