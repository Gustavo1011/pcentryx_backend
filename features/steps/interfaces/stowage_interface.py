"""
stowage_interface.py: Interface to generate stowages
"""
import time
from behave import given  # pylint: disable=import-error


@given('Importing stowage')
def importing_stowage(context):
    """ Importa una bodega activada """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data for create stowage
        When Creating stowage
        Then Satisfactory response 201
        And Saving stowage in global
    """)
    time.sleep(2)
