"""
__init__.py: Init file for classes
"""
import re
from sqlalchemy import event
from sqlalchemy.orm.attributes import set_committed_value
from sqlalchemy.orm.session import object_session

from models.user import User
from models.brand_component import BrandComponent
from models.brand_laptop import BrandLaptop
from models.cpu import Cpu
from models.graphic_card import GraphicCard
from models.instant_user import InstantUser
from models.minimal_type_service import MinimalTypeService
from models.model_laptop import ModelLaptop
from models.service import Service
from models.type_computer import TypeComputer
from models.type_defective_component import TypeDefectiveComponent
from models.type_service import TypeService
from models.type_sub_service import TypeSubService
from models.user_delivery import UserDelivery
from models.user_laptop_data import UserLaptopData
from models.user_pc_data import UserPcData
from models.user_request_defective_component import UserRequestDefectiveComponent
from models.user_request import UserRequest



from models.oauth2 import OAuthClient
from models.oauth2 import OAuthGrant
from models.oauth2 import OAuthToken


"""@event.listens_for(Subcategory, 'before_insert')
def generate_subcategory_code(mapper, connection, target):  # pylint: disable=unused-argument
        subcategory = Subcategory.query.filter(
        Subcategory.category.has(id=target.category_id),
        Subcategory.deleted == "false"
    ).order_by(Subcategory.code.desc()).limit(1).first()
    category = Category.query.with_entities(Category.code).filter_by(id=target.category_id).first()

    if subcategory is None:
        target.code = category.code + '001'
    else:
        target.code = category.code + str(int(subcategory.code[3:]) + 1).zfill(3)

@event.listens_for(Subcategory, 'before_update')
    def generate_subcategory_code_update(mapper, connection, target):  # pylint: disable=unused-argument
        subcategory = Subcategory.query.filter(
        Subcategory.category.has(id=target.category_id),
        Subcategory.deleted == "false"
    ).order_by(Subcategory.code.desc()).limit(1).first()
    category = Category.query.with_entities(Category.code).filter_by(id=target.category_id).first()
    
    if subcategory is None:
        target.code = category.code + '001'
    else:
        previous_category = Subcategory.query.filter_by(
                    id=target.id
                ).first()
        if previous_category.category_id!=target.category_id:
            target.code = category.code + str(previous_category.name).zfill(3) """

# @event.listens_for(ProductCategory, 'before_insert')
# def generate_product_category_code(mapper, connection, target): # pylint: disable=unused-argument
#     "listen for the 'before_insert' event"
#     category = ProductCategory.query.filter().order_by(ProductCategory.id.desc()).limit(1).first()
#     if category is None:
#         target.code = '001'
#     else:
#         target.code = str(category.id + 1).zfill(3)

# @event.listens_for(ProductSubcategory, 'before_insert')
# def generate_product_sub_category_code(mapper, connection, target): # pylint: disable=unused-argument
#     "listen for the 'before_insert' event"
#     category = ProductCategory.query.filter(
#         ProductCategory.id == target.product_category_id
#     ).first()
#     subcategory = category.product_subcategories.filter(
#     ).order_by(ProductSubcategory.id.desc()).limit(1).first()
#     if subcategory is None:
#         code_subcategory_relative = '001'
#     else:
#         code_subcategory_relative = str(int(subcategory.code[3:]) + 1).zfill(3)
#     target.code = category.code + code_subcategory_relative

# @event.listens_for(Requisition, 'before_insert')
# def generate_requisition_code(mapper, connection, target): # pylint: disable=unused-argument
#     "listen for the 'before_insert' event"
#     code = "RQ" + generate_code(Requisition, 6)
#     target.code = code

# @event.listens_for(Purchase, 'before_insert')
# def generate_purchase_code(mapper, connection, target): # pylint: disable=unused-argument
#     "listen for the 'before_insert' event"
#     code = "OC" + generate_code(Purchase, 7)
#     target.code = code

# @event.listens_for(PurchaseMove, 'before_insert')
# def generate_purchase_move_code(mapper, connection, target): # pylint: disable=unused-argument
#     "listen for the 'before_insert' event"
#     code = "TR" + generate_code(PurchaseMove, 7)
#     target.code = code

# @event.listens_for(PurchaseShipment, 'before_insert')
# def generate_purchase_shipment_code(mapper, connection, target): # pylint: disable=unused-argument
#     "listen for the 'before_insert' event"
#     code = "EMB" + generate_code(PurchaseShipment, 3)
#     target.code = code
