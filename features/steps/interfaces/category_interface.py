"""
manufactuter_interface.py: Interface to generate manufacturers
"""
import time
from behave import given # pylint: disable=import-error

@given('Importing category')
def importing_category(context):
    """ Importa una subcategoria """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data product category
        When Creating product category
        Then Satisfactory response 201
        And Saving product category in global
    """)
    time.sleep(2)

@given('Deleting product categories of global')
def deleting_product_categories_of_global(context):
    """ Elimina todas las categorias registradas en el global """
    count_product_categories = context.global_count('product_category')
    if count_product_categories is not None:
        for i in range(count_product_categories):
            context.execute_steps("""
                Given Integrating login module
                And Adding id in url for product category
                When Deleting product category
                Then Satisfactory response 200
                And Removing product category of global
            """)
