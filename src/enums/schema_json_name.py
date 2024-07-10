from enum import Enum


class SchemaName(Enum):
    get_customer_group = "get_customer_group.json"
    get_customer_groups_by_search_criteria_first_page_and_page_size = "get_customer_groups_by_search_criteria_first_page_and_page_size.json"
    post_customer = "post_customer_minimum_requirements.json"
    response_status_code_400_type_value_is_invalid = "response_status_code_400_type_value_is_invalid.json"
    response_status_code_404_no_such_entity = "response_status_code_404_no_such_entity.json"
    response_status_code_404_request_does_not_match = "response_status_code_404_request_does_not_match.json"
    post_customer_full_information = "post_customer_full_information.json"
    response_status_401_unauthorized = "response_status_401_unauthorized.json"
    put_customer_group_default = "put_customer_group_default.json"
    post_customer_group = "post_customer_group.json"