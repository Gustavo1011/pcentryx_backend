"""
agent_interface.py: Interface to generate agents
"""
import time
from behave import given # pylint: disable=import-error

@given('Importing agent')
def importing_agent(context):
    """ Importa un agente """
    context.execute_steps("""
        Given Integrating login module
        And Preparing valid data agent
        When Creating agent
        Then Satisfactory response 201
        And Saving agent in global
    """)
    time.sleep(2)

@given('Deleting agents of global')
def deleting_agents_of_global(context):
    """ Elimina todos los agentes registrados en el global """
    count_agents = context.global_count('agent')
    if count_agents is not None:
        for i in range(count_agents):
            context.execute_steps("""
                Given Integrating login module
                And Adding id in url for agent
                When Deleting agent
                Then Satisfactory response 200
                And Removing agent of global
            """)
