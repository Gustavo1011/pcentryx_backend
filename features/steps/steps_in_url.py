"""
steps_in_url.py: General steps of url for run tests
"""
from behave import given  # pylint: disable=import-error
from dotenv import load_dotenv  # pylint: disable=import-error

# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
load_dotenv("/app/.env")


@given('Adding value enable is_enabled in url')
def adding_value_enable_is_enabled_in_url(context):
    context.is_enabled = "true"


@given('Adding value disable is_enabled in url')
def adding_value_enable_is_disable_in_url(context):
    context.is_enabled = "false"


# Case: String
@given('Adding string enabled in url')
def adding_string_enabled_in_url(context):
    context.enabled = '&&$#$$//(/Jgjh'


@given('Adding string status in url')
def adding_string_status_in_url(context):
    context.status = 'asd'


@given('Adding string product_category_id in url')
def adding_string_product_category_id_in_url(context):
    context.product_category_id = 'asd'


@given('Adding string type_agent_id in url')
def adding_string_type_agent_id_in_url(context):
    context.type_agent_id = '&&$#$$//(/Jgjh'


@given('Adding string type_requisition_id in url')
def adding_string_type_requisition_id_in_url(context):
    context.type_requisition_id = 'asd'


@given('Adding string type_requisition_delivery_id in url')
def adding_string_type_requisition_delivery_id_in_url(context):
    context.type_requisition_delivery_id = 'asd'


@given('Adding string requisition_state_id in url')
def adding_string_requisition_state_id_in_url(context):
    context.requisition_state_id = 'asd'


@given('Adding string limit in url')
def adding_string_limit_in_url(context):
    context.limit = 'ass'


@given('Adding string page in url')
def adding_string_page_in_url(context):
    context.page = 'asc'


@given('Adding string id in url')
def adding_string_id_in_url(context):
    context.id = 'asd'


@given('Adding string company_id in url')
def adding_string_company_id_in_url(context):
    context.company_id = 'asd'


@given('Adding string product_id in url')
def adding_string_product_id_in_url(context):
    context.product_id = 'asd'


@given('Adding string country_id in url')
def adding_string_country_id_in_url(context):
    context.country_id = 'asd'


@given('Adding string provider_id in url')
def adding_string_provider_id_in_url(context):
    context.provider_id = 'asd'


@given('Adding string product_subcategory_id in url')
def adding_string_product_subcategory_id_in_url(context):
    context.product_subcategory_id = 'asd'


@given('Adding string analyst_id in url')
def adding_string_analyst_id_in_url(context):
    context.analyst_id = 'asd'


@given('Adding string assignment_analyst_id in url')
def adding_string_assignment_analyst_id_in_url(context):
    context.assignment_analyst_id = 'asd'


@given('Adding string assignment_product_category_id in url')
def adding_string_assignment_product_category_id_in_url(context):
    context.assignment_product_category_id = 'asd'


@given('Adding string product_subcategory_value_id in url')
def adding_string_product_subcategory_value_id_in_url(context):
    context.product_subcategory_value_id = 'asd'


@given('Adding string tracking_number_id in url')
def adding_string_tracking_number_id_in_url(context):
    context.tracking_number_id = 'asd'


@given('Adding string provider_quotation_id in url')
def adding_string_provider_quotation_in_url(context):
    context.provider_quotation_id = 'asd'


@given('Adding string purchase_move_id in url')
def adding_string_purchase_move_id_in_url(context):
    context.purchase_move_id = 'asd'


@given('Adding string purchase_warehouse_id in url')
def adding_string_purchase_warehouse_id_in_url(context):
    context.purchase_warehouse_id = 'asd'


@given('Adding string destination_agent_id in url')
def adding_string_destination_agent_id_in_url(context):
    context.destination_agent_id = 'asd'


@given('Adding string provider_main_product_id in url')
def adding_string_provider_main_product_id_in_url(context):
    context.provider_main_product_id = 'asd'


@given('Adding string provider_quotation_product_id in url')
def adding_string_provider_quotation_product_id_in_url(context):
    context.provider_quotation_product_id = 'asd'


# Case: Non-existent
@given('Adding non-existent document_id in url')
def adding_non_existent_document_id_in_url(context):
    context.document_id = '2147483648'


@given('Adding non-existent product_company_id in url')
def adding_non_existent_product_company_id_in_url(context):
    context.product_company_id = '2147483648'


@given('Adding non-existent destination_country_ids in url')
def adding_non_existent_destination_country_ids_in_url(context):
    context.destination_country_ids = '2147483648'


@given('Adding non-existent type_permission_ids in url')
def adding_non_existent_type_permission_ids_in_url(context):
    context.type_permission_ids = '2147483648'


@given('Adding non-existent requisition_ids in url')
def adding_non_existent_requisition_ids_in_url(context):
    context.requisition_ids = '2147483648'


@given('Adding non-existent purchase_warehouse_id in url')
def adding_non_existent_purchase_warehouse_id_in_url(context):
    context.purchase_warehouse_id = '2147483648'


@given('Adding non-existent type_agent_id in url')
def adding_non_existent_type_agent_id_in_url(context):
    context.type_agent_id = '2147483648'


@given('Adding non-existent provider_country_id in url')
def adding_non_existent_provider_country_id_in_url(context):
    context.provider_country_id = '2147483648'


@given('Adding non-existent type_requisition_id in url')
def adding_non_existent_type_requisition_id_in_url(context):
    context.type_requisition_id = '2147483648'


@given('Adding non-existent type_requisition_delivery_id in url')
def adding_non_existent_type_requisition_delivery_id_in_url(context):
    context.type_requisition_delivery_id = '2147483648'


@given('Adding non-existent requisition_state_id in url')
def adding_non_existent_requisition_state_id_in_url(context):
    context.requisition_state_id = '2147483648'


@given('Adding non-existent product_subcategory_value_id in url')
def adding_non_existent_product_subcategory_value_id_in_url(context):
    context.product_subcategory_value_id = '2147483648'


@given('Adding non-existent product_id in url')
def adding_non_existent_product_id_in_url(context):
    context.product_id = '2147483648'


@given('Adding non-existent country_id in url')
def adding_non_existent_country_id_in_url(context):
    context.country_id = '2147483648'


@given('Adding non-existent purchase_id in url')
def adding_non_existent_purchase_id_in_url(context):
    context.purchase_id = '2147483648'


@given('Adding non-existent id in url')
def adding_non_existent_id_in_url(context):
    context.id = '2147483648'


@given('Adding non-existent provider_id in url')
def adding_non_existent_provider_id_in_url(context):
    context.provider_id = '2147483648'


@given('Adding non-existent company_id in url')
def adding_non_existent_company_id_in_url(context):
    context.company_id = '2147483648'


@given('Adding non-existent product_subcategory_id in url')
def adding_non_existent_product_subcategory_id_in_url(context):
    context.product_subcategory_id = '2147483648'


@given('Adding non-existent assignment_analyst_id in url')
def adding_non_existent_assignment_analyst_id_in_url(context):
    context.assignment_analyst_id = 2147483648


@given('Adding non-existent assignment_product_category_id in_url')
def adding_non_existent_assignment_product_category_id_in_url(context):
    context.assignment_product_category_id = 2147483648


@given('Adding non-existent tracking_number_id in url')
def adding_non_existent_tracking_number_id_in_url(context):
    context.tracking_number_id = "2147483648"


@given('Adding non-existent provider_quotation_id in url')
def adding_non_existent_provider_quotation_id_in_url(context):
    context.provider_quotation_id = "2147483648"


@given('Adding non-existent purchase_move_id')
def adding_non_existent_purchase_move_id(context):
    context.purchase_move_id = '2147483648'


@given('Adding non-existent agent_id in url')
def adding_non_existent_agent_id_in_url(context):
    context.agent_id = '2147483648'


@given('Adding non-existent destination_agent_id in url')
def adding_non_existent_destination_agent_id_in_url(context):
    context.destination_agent_id = '2147483648'


@given('Adding non-existent provider_main_product_id in url')
def adding_non_existent_provider_main_product_id_in_url(context):
    context.provider_main_product_id = '2147483648'


@given('Adding non-existent provider_quotation_product_id in url')
def adding_non_existent_provider_quotation_product_id_in_url(context):
    context.provider_quotation_product_id = '2147483648'


@given('Adding non-existent purchase_move_id in url')
def adding_non_existent_purchase_move_id_in_url(context):
    context.purchase_move_id = '2147483648'


@given('Adding non-existent product_category_id in url')
def adding_non_existent_product_category_id_in_url(context):
    context.product_category_id = '2147483648'


# Case: Negative
@given('Adding negative product_category_id in url')
def adding_negative_product_category_id_in_url(context):
    context.product_category_id = '-1'


@given('Adding negative page in url')
def adding_negative_page_in_url(context):
    context.page = '-1'


@given('Adding negative limit in url')
def adding_negative_limit_in_url(context):
    context.limit = '-1'


@given('Adding negative product_id in url')
def adding_negative_product_id_in_url(context):
    context.product_id = '-1'


@given('Adding negative country_id in url')
def adding_negative_country_id_in_url(context):
    context.country_id = '-1'


@given('Adding negative type_agent_id in url')
def adding_negative_type_agent_id_in_url(context):
    context.type_agent_id = '-1'


@given('Adding negative id in url')
def adding_negative_id_in_url(context):
    context.id = '-1'


@given('Adding negative product_subcategory_id in url')
def adding_negative_product_subcategory_id_in_url(context):
    context.product_subcategory_id = '-1'


# Case: Integer
@given('Adding integer status in url')
def adding_integer_status_in_url(context):
    context.status = '12'


@given('Adding integer end_date in url')
def adding_integer_end_date_in_url(context):
    context.end_date = '12'


@given('Adding integer start_date in url')
def adding_integer_start_date_in_url(context):
    context.start_date = '12'


@given('Adding integer sort in url')
def adding_integer_sort_in_url(context):
    context.sort = '12'


@given('Adding integer order in url')
def adding_integer_order_in_url(context):
    context.order = '12'


# Case: Invalid value
@given('Adding invalid value order in url')
def adding_invalid_value_order_in_url(context):
    context.order = 'asd'


@given('Adding invalid value sort in url')
def adding_invalid_value_sort_in_url(context):
    context.sort = 'asd'


@given('Adding invalid value price_type in url')
def adding_invalid_value_price_type_in_url(context):
    context.price_type = '4'


@given('Adding invalid value transport in url')
def adding_invalid_value_transport_in_url(context):
    context.order = 'ground'


# Case: Value
@given('Adding value name sort in url')
def adding_value_name_sort_in_url(context):
    context.sort = 'name'


@given('Adding value company_name sort in url')
def adding_value_company_name_sort_in_url(context):
    context.sort = 'company_name'


@given('Adding value price sort in url')
def adding_value_price_sort_in_url(context):
    context.sort = 'price'


@given('Adding value country_name sort in url')
def adding_value_country_name_sort_in_url(context):
    context.sort = 'country_name'


@given('Adding value id sort in url')
def adding_value_id_sort_in_url(context):
    context.sort = 'id'


@given('Adding value enabled sort in url')
def adding_value_enabled_sort_in_url(context):
    context.sort = 'enabled'


@given('Adding value code sort in url')
def adding_value_code_sort_in_url(context):
    context.sort = 'code'


@given('Adding value product_category_name sort in url')
def adding_value_product_category_name_sort_in_url(context):
    context.sort = 'product_category_name'


@given('Adding value product_subcategory_name sort in url')
def adding_value_product_subcategory_name_sort_in_url(context):
    context.sort = 'product_subcategory_name'


@given('Adding value status sort in url')
def adding_value_status_sort_in_url(context):
    context.sort = 'status'


@given('Adding value brand_name sort in url')
def adding_value_brand_name_sort_in_url(context):
    context.sort = 'brand_name'


@given('Adding value product_name sort in url')
def adding_value_product_name_sort_in_url(context):
    context.sort = 'product_name'


@given('Adding value amount_request sort in url')
def adding_value_amount_request_sort_in_url(context):
    context.sort = 'amount_request'


@given('Adding value due_date sort in url')
def adding_value_due_date_sort_in_url(context):
    context.sort = 'due_date'


# Case: Decimal
@given('Adding decimal id in url')
def adding_decimal_id_in_url(context):
    context.id = '12.3'


@given('Adding decimal product_subcategory_id in url')
def adding_decimal_product_subcategory_id_in_url(context):
    context.product_subcategory_id = 1.5


# Case: Invalid char
@given('Adding invalid char id in url')
def adding_invalid_char_id_in_url(context):
    context.id = '%$&&&·'


@given('Adding invalid char company_id in url')
def adding_invalid_char_company_id_in_url(context):
    context.company_id = '%$&&&·'


@given('Adding invalid char product_subcategory_id in url')
def adding_invalid_char_product_subcategory_id_in_url(context):
    context.product_subcategory_id = '%$&&&·'


@given('Adding invalid char product_subcategory_value_id in url')
def adding_invalid_char_product_subcategory_value_id_in_url(context):
    context.product_subcategory_value_id = '%$&&&·'


# Case: Removing
@given('Removing destination_country_ids of url')
def removing_destination_country_ids_of_url(context):
    context.destination_country_ids = ''


@given('Removing transport of url')
def removing_transport_of_url(context):
    context.transport = ''


@given('Removing status of url')
def removing_status_of_url(context):
    context.status = ''


@given('Removing provider_country_id of url')
def removing_provider_country_id_of_url(context):
    context.provider_country_id = ''


@given('Removing price_type of url')
def removing_price_type_of_url(context):
    context.price_type = ''


@given('Removing product_category_id of url')
def removing_product_category_id_of_url(context):
    context.product_category_id = ''


@given('Removing country_id of url')
def removing_country_id_of_url(context):
    context.country_id = ''


@given('Removing type_agent_id of url')
def removing_type_agent_id_of_url(context):
    context.type_agent_id = ''


@given('Removing requisition_state_id of url')
def removing_requisition_state_id_of_url(context):
    context.requisition_state_id = ''


@given('Removing product_subcategory_value_id of url')
def removing_product_subcategory_value_id_of_url(context):
    context.product_subcategory_value_id = ''


@given('Removing company_id of url')
def removing_company_id_of_url(context):
    context.company_id = ''


@given('Removing product_subcategory_id of url')
def removing_product_subcategory_id_of_url(context):
    context.product_subcategory_id = ''


@given('Removing id in url')
def removing_id_in_url(context):
    context.id = ''


@given('Removing provider_quotation_product_id in url')
def removing_provider_quotation_product_id_in_url(context):
    context.provider_quotation_product_id = ''


@given('Removing purchase_warehouse_id in url')
def removing_purchase_warehouse_id_in_url(context):
    context.purchase_warehouse_id = ''


@given('Removing purchase_move_id in url')
def removing_purchase_move_id_in_url(context):
    context.purchase_move_id = ''


@given('Removing country_id in url')
def removing_country_id_in_url(context):
    del context.country_id


# Case: Invalid format
@given('Adding invalid format destination_country_ids in url')
def adding_invalid_format_destination_country_ids_in_url(context):
    context.destination_country_ids = '1111.11'


@given('Adding invalid format type_permission_ids in url')
def adding_invalid_format_type_permission_ids_in_url(context):
    context.type_permission_ids = '1111.11'


@given('Adding invalid format requisition_ids in url')
def adding_invalid_format_requisition_ids_in_url(context):
    context.requisition_ids = '1111.11'


@given('Adding invalid format start_date in url')
def adding_invalid_format_start_date_in_url(context):
    context.start_date = '2050-01-01 00:00:00.000000+00:00'


@given('Adding invalid format end_date in url')
def adding_invalid_format_end_date_in_url(context):
    context.end_date = '2050-01-01 00:00:00.000000+00:00'


# Case: Especial
@given('Adding company_id in url')
def adding_company_id_in_url(context):
    context.company_id = '1'


@given('Adding stowage_id in url')
def adding_stowage_id_in_url(context):
    context.stowage_id = str(context.global_get('stowage')['id'])


@given('Adding disabled analyst_id in url')
def adding_disabled_analyst_id_in_url(context):
    context.analyst_id = '1'


@given('Adding enabled analyst_id in url')
def adding_enabled_analyst_id_in_url(context):
    context.analyst_id = '2'


@given('Adding invalid analyst_id in url')
def adding_invalid_analyst_id_in_url(context):
    context.analyst_id = '3'


@given('Adding standar price_type in url')
def adding_standar_price_type_in_url(context):
    context.price_type = '1'


@given('Adding special price_type in url')
def adding_special_price_type_in_url(context):
    context.price_type = '2'


@given('Adding volume price_type in url')
def adding_volume_price_type_in_url(context):
    context.price_type = '3'


@given('Adding bad format type_document_categories in url')
def adding_bad_format_type_document_categories_in_url(context):
    context.type_document_categories = '3,2.3.4'


@given('Adding non-existent {key} in url')
def adding_non_existent_key_in_url(context, key):
    setattr(context, key, '2147483648')


@given('Adding string {key} in url')
def adding_string_key_in_url(context, key):
    setattr(context, key, 'value')


@given('Adding positive decimal {key} in url')
def adding_positive_decimal_key_in_url(context, key):
    setattr(context, key, '1.11')


@given('Adding negative integer {key} in url')
def adding_negative_integer_key_in_url(context, key):
    setattr(context, key, '-1')


@given('Adding positive integer {key} in url')
def adding_positive_integer_key_in_url(context, key):
    setattr(context, key, '1')


@given('Adding empty string {key} in url')
def adding_empty_string_key_in_url(context, key):
    setattr(context, key, '')


@given('Adding value {value} {key} in url')
def adding_value_value_key_in_url(context, value, key):
    setattr(context, key, value)


@given('Adding invalid value {key} in url')
def adding_invalid_value_key_in_url(context, key):
    setattr(context, key, 'invalid')


@given('Adding invalid date {key} in url')
def adding_invalid_date_key_in_data(context, key):
    setattr(context, key, '12-12-2018')
