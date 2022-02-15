"""
subcategory_interface.py: Interface to generate subcategories
"""
import time
from behave import given # pylint: disable=import-error

@given('Importing subcategory')
def importing_subcategory(context):
    """ Importa una subcategoria """
    context.execute_steps("""
        Given Importing category
        And Integrating login module
        And Preparing valid data product subcategory and values
        When Creating product subcategory
        Then Satisfactory response 201
        And Saving product subcategory in global
    """)
    time.sleep(2)
