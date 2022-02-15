from behave import given
from dotenv import load_dotenv
load_dotenv("/app/.env")

@given('Integrating login module {user}')
def integrating_login_module_(context, user):
    context.execute_steps('''
        Given Preparing valid data {}
        When Logging in
        Then Session created
    '''.format(user))

# @given('Integrating login module with timezone {timezone}')
# def integrating_login_module_with_timezone(context, timezone):
#     context.execute_steps('''
#         Given Preparing valid data admin
#         And Adding value {} timezone in url
#         When Logging in
#         Then Session created
#     '''.format(timezone))
