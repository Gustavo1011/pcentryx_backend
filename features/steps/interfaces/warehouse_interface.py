"""
warehouse_interface.py: Interface to generate warehouses
"""
import time
from behave import given  # pylint: disable=import-error


@given('Importing warehouse')
def importing_warehouse(context):
    """ Importa un almacen desactivado """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data for create warehouse
        When Creating warehouse
        Then Satisfactory response 201
        And Saving warehouse in global
    """)
    time.sleep(2)
