import os
import json
from behave import given, when, then
import requests
from dotenv import load_dotenv
load_dotenv("/app/.env")

@given('Preparing valid data {user}')
def preparing_valid_data(context, user):
    context.datos = {'username': user, 'password': '123456'}
    context.timezone = 'UTC'

@when('Logging in')
def logging_in(context):
    print(context.datos)
    context.response = requests.post(
        url=os.getenv('BASE_URL', "") + '/erp/login/',
        json=context.datos,
        headers={
            'content_type': 'application/json',
            'timezone': context.timezone
        }
    )

@then('Session created')
def session_created(context):
    response = context.response.text
    response_string = json.loads(response)
    context.key_login = 'Bearer ' + str(response_string['result']['access_token'])
    if context.response.status_code != 200:
        raise Exception('Response status not passed\nStatus code should be 200')

@given('Preparing invalid data')
def preparing_invalid_data(context):
    context.datos = {'username': '', 'password': ''}

@then('Session failed')
def session_failed(context):
    if context.response.status_code != 400:
        raise Exception('Response status not passed\nStatus code should be 400')

@given('Preparing invalid data without username')
def preparing_invalid_data_without_username(context):
    context.datos = {'username': 'xxxxxxxx', 'password': '123456'}

@given('Preparing invalid data without password')
def preparing_invalid_data_without_password(context):
    context.datos = {'username': 'admin', 'password': 'xxxxxxxx'}
