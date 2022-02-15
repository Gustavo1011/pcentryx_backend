"""
brand_interface.py: Interface to generate brands
"""
import time
from behave import given # pylint: disable=import-error

@given('Importing brand')
def importing_brand(context):
    """ Importa una marca """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data for create brand
        When Creating brand
        Then Satisfactory response 201
        And Saving brand in global
    """)
    time.sleep(2)
