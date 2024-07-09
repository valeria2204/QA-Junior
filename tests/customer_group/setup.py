import json

import pytest

from src.enums.method import Method
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from src.testdata import TestData
from tests.conftest import get_token_login
from tests.helpers.utils import Utils


@pytest.fixture(scope="function")
def teardown_function_remove_customer_group():
    TestData.token = get_token_login() if TestData.token is None else TestData.token

    def teardown():
        if "id" in TestData.function_response_json_customer_group:
            send_request_of_remove_customer_group(TestData.function_response_json_customer_group["id"])

    yield TestData.token
    teardown()


@pytest.fixture(scope="function")
def setup_function_customer_group():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    TestData.random_value = Utils().get_random_alphanumeric(5)
    TestData.function_response_json_customer_group = None
    TestData.function_response_json_customer_group = send_request_of_create_a_customer_group(f"CODE_{TestData.random_value}")

    def teardown():
        send_request_of_remove_customer_group(TestData.function_response_json_customer_group["id"])
    yield TestData.token
    teardown()


@pytest.fixture(scope="module")
def setup_module_customer_group():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    TestData.random_value = Utils().get_random_alphanumeric(5)
    TestData.module_response_json_customer_group = None
    TestData.module_response_json_customer_group = send_request_of_create_a_customer_group(f"CODE_{TestData.random_value}")

    def teardown():
        send_request_of_remove_customer_group(TestData.module_response_json_customer_group["id"])
    yield TestData.token
    teardown()


def send_request_of_create_a_customer_group(code):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.POST_CUSTOMER_GROUP.value}"

    payload = json.dumps({
        "group": {
            "code": f"{code}"
        }
    })

    headers = header_content_type_authorization(TestData.token)
    response = TestData.request_client(Method.POST.value, url, headers, payload).run()
    TestData.response_status_code = response.status_code

    return response.json()


def send_request_of_remove_customer_group(group_id, token=None, method="DELETE"):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.DELETE_CUSTOMER_GROUP.value}".replace(
        URIComplement.GROUP_ID_KEY_NAME.value, f"{group_id}")

    payload = {}
    if token is None:
        token = TestData.token
    headers = header_authorization(token)
    response = TestData.request_client(method, url, headers, payload).run()
    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_obtain_customer_groups_by_search_criterias(current_page=None, page_size=None, field=None,
                                                               value=None, condition=None, token=None, method=None, headers=None,
                                                               payload=None):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}"

    params = {}
    if current_page is not None:
        params[URIComplement.SEARCH_CRITERIA_PARAMETER_CURRENT_PAGE.value] = current_page
    if page_size is not None:
        params[URIComplement.SEARCH_CRITERIA_PARAMETER_PAGE_SIZE.value] = page_size
    if field is not None:
        params[URIComplement.SEARCH_CRITERIA_PARAMETER_FIELD.value] = field
    if value is not None:
        params[URIComplement.SEARCH_CRITERIA_PARAMETER_VALUE.value] = value
    if condition is not None:
        params[URIComplement.SEARCH_CRITERIA_PARAMETER_CONDITION.value] = condition
    if method is None:
        method = Method.GET.value

    if token is None:
        token = TestData.token
    if payload is None:
        payload = {}
    if headers is None:
        headers = header_authorization(token)

    response = TestData.request_client(method, url, headers, payload, params).run()

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_obtain_customer_group_by_id(group_id, token=None):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_ID.value}".replace(
        URIComplement.GROUP_ID_KEY_NAME.value, str(group_id))

    payload = {}
    if token is None:
        token = TestData.token
    headers = header_authorization(token)
    response = TestData.request_client(Method.GET.value, url, headers, payload).run()
    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_obtain_default_customer_group_by(token=None, headers=None, payload=None, last_parameter=None):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_DEFAULT.value}"

    if token is None:
        token = TestData.token
    if payload is None:
        payload = {}
    if headers is None:
        headers = header_authorization(token)
    if last_parameter is not None:
        url = url + last_parameter
    response = TestData.request_client(Method.GET.value, url, headers, payload).run()

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_obtain_default_customer_group_by_store_id(store_id, token=None, method=None, headers=None,
                                                              payload=None):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(
        URIComplement.STORE_ID_KEY_NAME.value, f"{store_id}")

    if token is None:
        token = TestData.token
    if payload is None:
        payload = {}
    if headers is None:
        headers = header_authorization(token)
    if method is None:
        method = Method.GET.value
    response = TestData.request_client(method, url, headers, payload).run()

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_check_if_customer_group_can_be_deleted_with_group_id(group_id, method=None, token=None):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.GET_CHECK_DELETION_CUSTOMER_GROUP.value}".replace(
        URIComplement.GROUP_ID_KEY_NAME.value, f"{group_id}")

    if token is None:
        token = TestData.token
    if method is None:
        method = Method.GET.value
    payload = {}
    headers = header_authorization(token)
    response = TestData.request_client(method, url, headers, payload).run()

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_update_customer_group(group_id, code_group, tax_class_id, token=None):
    url = f"{TestData.base_url}{URIComplement.PUT_CUSTOMER_GROUP.value}".replace(
        URIComplement.GROUP_ID_KEY_NAME.value, f"{group_id}")
    if token is None:
        token = TestData.token

    payload = json.dumps({
        "group": {
            "id": group_id,
            "code": code_group,
            "tax_class_id": tax_class_id
        }
    })

    headers = header_content_type_authorization(token)
    response = TestData.request_client(Method.PUT.value, url, headers, payload).run()
    TestData.response_status_code = response.status_code

    return response.json()


def send_request_of_update_customer_group_default(group_id, token=None, method=None):
    if token is None:
        token = TestData.token
    if method is None:
        method = Method.PUT.value
    url = f"{TestData.base_url}{URIComplement.PUT_CUSTOMER_GROUP_DEFAULT.value.replace('{id}', str(group_id))}"
    headers = header_content_type_authorization(token)
    response = TestData.request_client(method, url, headers=headers).run()
    TestData.response_status_code = response.status_code
    return response.json()



