"""
general.py: General Steps
"""
import json
from behave import then
from dotenv import load_dotenv
load_dotenv("/app/.env")

# pylint: disable=missing-function-docstring
@then('Satisfactory response 200')
def satisfactory_response_200(context):
    if context.response.status_code != 200:
        print(context.response.text)
        raise Exception('Response status not passed\nStatus code should be 200')

@then('Satisfactory response 201')
def satisfactory_response_201(context):
    if context.response.status_code != 201:
        print(context.response.text)
        raise Exception('Response status not passed\nStatus code should be 201')

@then('Error 400')
def error_400(context):
    if context.response.status_code != 400:
        print(context.response.text)
        raise Exception('Response status not passed\nStatus code should be 400')

@then('Error 404')
def error_404(context):
    if context.response.status_code != 404:
        raise Exception('Response status not passed\nStatus code should be 404')

@then('Error 405')
def error_405(context):
    if context.response.status_code != 405:
        raise Exception('Response status not passed\nStatus code should be 405')

@then('Checking the error field {key1} of {key2} of {key3}')
def checking_the_error_field_key1_of_key2_of_key3(context, key1, key2, key3):
    errors = json.loads(context.response.text)['errors']
    for error in errors:
        if key3 == error['field']:
            if key2 == error['extra']['field']:
                if key1 == error['extra']['extra']['field']:
                    break
    else:
        print(error)
        raise Exception('Response status not passed\nIncorrect message error')

@then('Checking the error field {key1} of {key2}')
def checking_the_error_field_key1_of_key2(context, key1, key2):
    errors = json.loads(context.response.text)['errors']
    for error in errors:
        if key2 == error['field']:
            if key1 == error['extra']['field']:
                break
    else:
        print(error)
        raise Exception('Response status not passed\nIncorrect message error')

@then('Checking the error field {key}')
def checking_the_error_field_key(context, key):
    print(json.loads(context.response.text))
    errors = json.loads(context.response.text)['errors']
    for error in errors:
        if key == error['field']:
            break
    else:
        print(error)
        raise Exception('Response status not passed\nIncorrect message error')
