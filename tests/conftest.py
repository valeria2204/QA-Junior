import json
import pytest
import requests

from src.enums.method import Method
from src.enums.uri import URIComplement
from src.headers.headers import header_authorization, header_content_type_authorization, header_content_type
from src.testdata import TestData


@pytest.fixture
def setup_data():
    TestData.token = get_token_login() if TestData.token is None else TestData.token


def get_token_login():
    TestData.load_attributes_from_json()
    url = f"{TestData.base_url}{URIComplement.POST_GET_TOKEN.value}"
    headers = header_content_type()
    payload = json.dumps({
        "username": TestData.username,
        "password": TestData.password
    })
    response = requests.request(Method.POST.value, url, headers=headers, data=payload)
    return response.json()


def send_request_of_obtain_customer_groups_by_search_criteria_first_page_and_page_size(current_page: str, page_size: str):
    url = (f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}?"
           f"{URIComplement.SEARCH_CRITERIA_PARAMETER_CURRENT_PAGE.value.replace(URIComplement.CURRENT_PAGE_KEY_NAME.value, current_page)}&"
           f"{URIComplement.SEARCH_CRITERIA_PARAMETER_PAGE_SIZE.value.replace(URIComplement.PAGE_SIZE_KEY_NAME.value, page_size)}")

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.GET.value, url, headers=headers, data=payload)

    TestData.response_json = json.loads(response.text)
    TestData.response_status_code = response.status_code


def send_request_of_obtain_customer_group_by_id(group_id):
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_ID.value}".replace(URIComplement.GROUP_ID_KEY_NAME.value, group_id)

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.GET.value, url, headers=headers, data=payload)

    TestData.response_json = json.loads(response.text)
    TestData.response_status_code = response.status_code


def send_request_of_create_a_customer(
        email: str
        , firstname: str
        , lastname: str
        , group_id=1
        , default_billing="2024-04-07 23:49:59"
        , default_shipping="2024-04-07 23:49:59"
        , created_at="2024-04-07 23:49:59"
        , updated_at="2024-04-07 23:49:59"
        , created_in="Default Store View"
        , dob="2024-04-17"
        , middlename="MN"
        , prefix="P"
        , suffix="S"
        , gender=1
        , store_id=1
        , website_id=1
        , addresses=[]
        , disable_auto_group_change=0
        , password="Password123#"
        , redirectUrl="string"
):
    url = f"{TestData.base_url}{URIComplement.POST_CUSTOMER.value}"

    payload = json.dumps({
        "customer": {
            "group_id": group_id,
            "default_billing": default_billing,
            "default_shipping": default_shipping,
            "created_at": created_at,
            "updated_at": created_at,
            "created_in": created_in,
            "dob": dob,
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
            "middlename": middlename,
            "prefix": prefix,
            "suffix": suffix,
            "gender": gender,
            "store_id": store_id,
            "website_id": website_id,
            "addresses": addresses,
            "disable_auto_group_change": disable_auto_group_change
        },
        "password": password,
        "redirectUrl": redirectUrl
    })
    headers = header_content_type_authorization(TestData.token)
    response = requests.request(Method.POST.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    TestData.response_json = json.loads(response.text)


def send_request_of_check_if_customer_group_can_be_deleted_with_group_id(group_id, method, token):
    url = f"{TestData.base_url}{URIComplement.GET_CHECK_DELETION_CUSTOMER_GROUP.value}".replace(URIComplement.GROUP_ID_KEY_NAME.value, group_id)

    payload = {}
    headers = header_authorization(token)
    response = requests.request(method, url, headers=headers, data=payload)

    TestData.response_json = json.loads(response.text)
    TestData.response_status_code = response.status_code




