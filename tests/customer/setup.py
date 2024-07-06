import json

import pytest
import requests

from src.enums.method import Method
from src.enums.static_data import StaticData
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from src.testdata import TestData
from tests.conftest import get_token_login
from tests.helpers.utils import Utils


@pytest.fixture(scope="function")
def setup_function():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    TestData.random_email = f"{Utils().get_random_alphanumeric(10)}@gmail.com"
    TestData.function_response_json = send_request_of_create_a_customer(TestData.random_email,
                                                                        StaticData.firstname.value,
                                                                        StaticData.lastname.value)

    def teardown():
        send_request_of_remove_customer(TestData.function_response_json["id"])
    yield TestData.token
    teardown()


@pytest.fixture(scope="module")
def setup_module_customer_with_account():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    TestData.random_email = f"{Utils().get_random_alphanumeric(10)}@gmail.com"
    TestData.module_response_json = send_request_of_create_a_customer(
        TestData.random_email
        , StaticData.firstname.value
        , StaticData.lastname.value
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , None
        , StaticData.password.value
        , None
    )

    def teardown():
        send_request_of_remove_customer(TestData.module_response_json["id"])
    yield TestData.token
    teardown()


def send_request_of_remove_customer(customer_id):
    url = f"{TestData.base_url}{URIComplement.DELETE_CUSTOMER.value.replace(URIComplement.CUSTOMER_ID_KEY_NAME.value, str(customer_id))}"

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.DELETE.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    return response.json()


@pytest.fixture(scope="module")
def setup_module():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    TestData.random_email = f"{Utils().get_random_alphanumeric(10)}@gmail.com"
    TestData.module_response_json = send_request_of_create_a_customer(TestData.random_email,
                                                                        StaticData.firstname.value,
                                                                        StaticData.lastname.value)

    def teardown():
        send_request_of_remove_customer(TestData.module_response_json["id"])
    yield TestData.token
    teardown()


def send_request_of_remove_customer(customer_id):
    url = f"{TestData.base_url}{URIComplement.DELETE_CUSTOMER.value.replace(URIComplement.CUSTOMER_ID_KEY_NAME.value, str(customer_id))}"

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.DELETE.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_create_a_customer(
        email: str
        , firstname: str
        , lastname: str
        , group_id=None
        , default_billing=None
        , default_shipping=None
        , created_at=None
        , updated_at=None
        , created_in=None
        , dob=None
        , middlename=None
        , prefix=None
        , suffix=None
        , gender=None
        , store_id=None
        , website_id=None
        , addresses=None
        , disable_auto_group_change=None
        , password=None
        , redirect_url=None
):
    url = f"{TestData.base_url}{URIComplement.POST_CUSTOMER.value}"

    payload = {StaticData.customer.name: StaticData.customer.value}
    if email is not None:
        payload[StaticData.customer.name][StaticData.email.name] = email
    if firstname is not None:
        payload[StaticData.customer.name][StaticData.firstname.name] = firstname
    if lastname is not None:
        payload[StaticData.customer.name][StaticData.lastname.name] = lastname
    if group_id is not None:
        payload[StaticData.customer.name][StaticData.group_id.name] = group_id
    if default_billing is not None:
        payload[StaticData.customer.name][StaticData.default_billing.name] = default_billing
    if default_shipping is not None:
        payload[StaticData.customer.name][StaticData.default_shipping.name] = default_shipping
    if created_at is not None:
        payload[StaticData.customer.name][StaticData.created_at.name] = created_at
    if updated_at is not None:
        payload[StaticData.customer.name][StaticData.updated_at.name] = updated_at
    if created_in is not None:
        payload[StaticData.customer.name][StaticData.created_in.name] = created_in
    if dob is not None:
        payload[StaticData.customer.name][StaticData.dob.name] = dob
    if middlename is not None:
        payload[StaticData.customer.name][StaticData.middlename.name] = middlename
    if prefix is not None:
        payload[StaticData.customer.name][StaticData.prefix.name] = prefix
    if suffix is not None:
        payload[StaticData.customer.name][StaticData.suffix.name] = suffix
    if gender is not None:
        payload[StaticData.customer.name][f'{gender=}'.split('=')[0]] = gender
    if store_id is not None:
        payload[StaticData.customer.name][f'{store_id=}'.split('=')[0]] = store_id
    if website_id is not None:
        payload[StaticData.customer.name][f'{website_id=}'.split('=')[0]] = website_id
    if addresses is not None:
        payload[StaticData.customer.name][f'{addresses=}'.split('=')[0]] = addresses
    if disable_auto_group_change is not None:
        payload[StaticData.customer.name][StaticData.disable_auto_group_change.name] = disable_auto_group_change
    if password is not None:
        payload[StaticData.password.name] = password
    if redirect_url is not None:
        payload[StaticData.redirectUrl.name] = redirect_url

    headers = header_content_type_authorization(TestData.token)
    response = requests.request(Method.POST.value, url, headers=headers, data=json.dumps(payload))

    TestData.response_status_code = response.status_code
    return json.loads(response.text)


def send_request_for_assign_a_new_cart_to_a_customer(customer_id):
    url = f"{TestData.base_url}{URIComplement.POST_CART_TO_CUSTOMER.value.replace(URIComplement.CUSTOMER_ID_KEY_NAME.value, str(customer_id))}"

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.POST.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_update_password_of_a_customer(customer_id, new_password, old_password):
    url = f"{TestData.base_url}{URIComplement.PUT_PASSWORD_CUSTOMER.value}".replace(
        URIComplement.CUSTOMER_ID_KEY_NAME.value, f"{customer_id}")

    params = {URIComplement.PATH_PARAMETER_CUSTOMER_ID.value: customer_id}

    payload = json.dumps({
        "currentPassword": old_password,
        "newPassword": new_password
    })

    headers = header_content_type_authorization(TestData.token)
    response = requests.request(Method.PUT.value, url, headers=headers, data=payload, params=params)
    TestData.response_status_code = response.status_code

    return response.json()
