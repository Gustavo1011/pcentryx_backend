"""
steps_in_data.py: General steps of data for run tests
"""
import time
from datetime import datetime, timedelta
from behave import given
from dotenv import load_dotenv
load_dotenv("/app/.env")
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

@given('Adding phone {key} in data')
def adding_phone_key_in_data(context, key):
    context.data[key] = '983-435-235'

@given('Adding integer {key} in data')
def adding_integer_key_in_data(context, key):
    context.data[key] = 1

@given('Adding spacing {key} in data')
def adding_spacing_key_in_data(context, key):
    context.data[key] = ' va  lu e  ' + str(time.time())

@given('Adding ticked {key} in data')
def adding_ticked_key_in_data(context, key):
    context.data[key] = 'áéíóúñ' + str(time.time())

@given('Adding capitalized {key} in data')
def adding_capitalized_key_in_data(context, key):
    context.data[key] = 'VALUE' + str(time.time())

@given('Adding dotted {key} in data')
def adding_dotted_key_in_data(context, key):
    context.data[key] = 'v.a.l.u.e' + str(time.time())

@given('Adding value string {key1} of first {key2} of first {key3} in data')
def adding_value_string_key1_of_first_key2_of_first_key3_in_data(context, key1, key2, key3):
    context.data[key3][0][key2][0][key1] = key1

@given('Adding value higher than allowed {key1} of first {key2} of first {key3} in data')
def adding_value_hta_key1_of_first_key2_of_first_key3_in_data(context, key1, key2, key3):
    context.data[key3][0][key2][0][key1] = 2147483649

@given('Adding value negative {key1} of first {key2} of first {key3} in data')
def adding_value_negative_key1_of_first_key2_of_first_key3_in_data(context, key1, key2, key3):
    context.data[key3][0][key2][0][key1] = -1

@given('Adding value non-existent {key1} of first {key2} of first {key3} in data')
def adding_value_non_existent_key1_of_first_key2_of_first_key3_in_data(context, key1, key2, key3):
    context.data[key3][0][key2][0][key1] = 2147483648

@given('Adding value non-existent in array {key1} of first {key2} in data')
def adding_value_non_existent_key1_of_first_key2_in_data(context, key1, key2):
    context.data[key2][0][key1] = [2147483648, 2147483647]

@given('Adding value repeated in array {key1} of first {key2} in data')
def adding_value_repeated_key1_of_first_key2_in_data(context, key1, key2):
    context.data[key2][0][key1] = [1, 1, 1]

@given('Adding value true {key1} of first {key2} in data')
def adding_value_true_key1_of_first_key2_in_data(context, key1, key2):
    context.data[key2][0][key1] = True

@given('Adding positive integer {key_1} of first {key_2} in data')
def adding_positive_integer_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = 1

@given('Adding positive integer {key} in data')
def adding_positive_integer_key_in_data(context, key):
    context.data[key] = 1

@given('Adding negative integer {key_1} of first {key_2} in data')
def adding_negative_integer_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = -1

@given('Adding negative integer {key_1} of {key_2} in data')
def adding_negative_integer_key_1_of_key_2_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = -1

@given('Adding negative integer array {key} in data')
def adding_negative_integer_array_key_in_data(context, key):
    context.data[key] = [-1]

@given('Adding negative integer {key} in data')
def adding_negative_integer_key_in_data(context, key):
    context.data[key] = -1

@given('Adding negative decimal {key_1} of first {key_2} in data')
def adding_negative_decimal_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = -1.11

@given('Adding not allowed {key_1} of first {key_2} in data')
def adding_not_allowed_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = '#$%@?¡°!¿/-_+-*'

@given('Adding not allowed {key} in data')
def adding_not_allowed_key_in_data(context, key):
    context.data[key] = '#$%@?¡°!¿/-_+-*'

@given('Adding very big {key_1} of first {key_2} in data')
def adding_very_big_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = 'a' * 350

@given('Adding very big {key} in data')
def adding_very_big_key_in_data(context, key):
    context.data[key] = 'a' * 350

@given('Adding empty string {key_1} of first {key_2} in data')
def adding_empty_string_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = ''

@given('Adding empty {type} {key_1} of {key_2} in data')
def adding_empty_type_key_1_of_key_2_in_data(context, type, key_1, key_2):
    if type == 'string':
        context.data[key_2][0][key_1] = ''
    elif type == 'array':
        context.data[key_2][0][key_1] = []

@given('Adding empty {type} {key} in data')
def adding_empty_type_key_in_data(context, type, key):
    if type == 'string':
        context.data[key] = ''
    elif type == 'array':
        context.data[key] = []

@given('Adding string {key_1} of first {key_2} in data')
def adding_string_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = 'value'

@given('Adding string array {key} in data')
def adding_string_array_key_in_data(context, key):
    context.data[key] = ['value']

@given('Adding string {key} in data')
def adding_string_key_in_data(context, key):
    context.data[key] = 'value'

@given('Adding positive decimal {key_1} of first {key_2} in data')
def adding_positive_decimal_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = 1.11

@given('Adding positive decimal {key} in data')
def adding_positive_decimal_key_in_data(context, key):
    context.data[key] = 1.11

@given('Adding null {key_1} of first {key_2} in data')
def adding_null_key_of_first_key_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = None

@given('Adding null {key_1} of {key_2} in data')
def adding_null_key_1_of_key_2_in_data(context, key_1, key_2):
    context.data[key_2][0][key_1] = None

@given('Adding null {key} in data')
def adding_null_key_in_data(context, key):
    context.data[key] = None

@given('Removing field {key_1} of first {key_2} of first {key_3} in data')
def removing_field_key_1_of_first_key_2_of_first_key_3_in_data(context, key_1, key_2, key_3):
    del context.data[key_3][0][key_2][0][key_1]

@given('Removing field {key_1} of first {key_2} in data')
def removing_field_key_1_of_first_key_2_in_data(context, key_1, key_2):
    del context.data[key_2][0][key_1]

@given('Removing field {key_1} of {key_2} in data')
def removing_field_key_1_of_key_2_in_data(context, key_1, key_2):
    del context.data[key_2][0][key_1]

@given('Removing field {key} in data')
def removing_field_key_in_data(context, key):
    del context.data[key]

@given('Adding dated {days} days ago {key} in data')
def adding_dated_days_days_ago_key_in_data(context, days, key):
    date_time = datetime.utcnow() - timedelta(days=int(days))
    date_time = datetime.combine(date_time, datetime.min.time())
    context.data[key] = date_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

@given('Adding dated after {days} days {key} in data')
def adding_dated_after_days_key_in_data(context, days, key):
    date_time = datetime.utcnow() + timedelta(days=int(days))
    date_time = datetime.combine(date_time, datetime.min.time())
    context.data[key] = date_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

@given('Adding current day {key} in data')
def adding_current_day_key_in_data(context, key):
    date_time = datetime.utcnow()
    date_time = datetime.combine(date_time, datetime.min.time())
    context.data[key] = date_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

@given('Adding value decimal {value} in {key_1} of first {key_2} in data')
def adding_value_decimal_value_in_key_of_first_key_in_data(context, value, key_1, key_2):
    context.data[key_2][0][key_1] = float(value)

@given('Adding value integer {value} in {key_1} of first {key_2} in data')
def adding_value_integer_value_in_key_of_first_key_in_data(context, value, key_1, key_2):
    context.data[key_2][0][key_1] = int(value)

@given('Adding value string {value} in {key_1} of first {key_2} in data')
def adding_value_string_value_in_key_of_first_key_in_data(context, value, key_1, key_2):
    context.data[key_2][0][key_1] = value

@given('Adding value string {value} in {key} in data')
def adding_value_string_value_in_key_in_data(context, value, key):
    context.data[key] = value

@given('Adding value decimal {value} in {key} in data')
def adding_value_decimal_value_in_key_in_data(context, value, key):
    context.data[key] = float(value)

@given('Adding non-existent {key_1} of {key_2} in data')
def adding_non_existent_key_1_of_key_2_in_data(context, key_1, key_2):
    if key_1 == "value":
        context.data[key_2].append(2147483648)
    else:
        context.data[key_2][0][key_1] = 2147483648

@given('Adding non-existent {key} in data')
def adding_non_existent_key_in_data(context, key):
    context.data[key] = 2147483648

@given('Adding repeated value of {key} in data')
def adding_repeated_value_of_key_in_data(context, key):
    context.data[key] = [1, 1]

@given('Adding repeated array {key} in data')
def adding_repeated_array_key_in_data(context, key):
    context.data[key] = [1, 1]

@given('Adding invalid date {key} in data')
def adding_invalid_date_key_in_data(context, key):
    context.data[key] = '12-12-2018'

@given('Adding boolean {} in data')
def adding_boolean_key_in_data(context, key):
    context.data[key] = True
