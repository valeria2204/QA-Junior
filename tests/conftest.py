import json

import pytest
import requests

from src.singleton import Singleton


@pytest.fixture
def get_token_login():
    url = Singleton.get_base_url() + "/rest/default/V1/integration/admin/token"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({
        "username": Singleton.get_username(),
        "password": Singleton.get_password()
    })
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def get_body_of_create_a_customer_with_basic_information(get_token_login):
    token = get_token_login
    url = Singleton.get_base_url() + "/rest/default/V1/customers"
    payload = json.dumps({
        "customer": {
            "email": f"{Singleton.get_random_alphanumeric(4)}@gmail.com",
            "firstname": "jorge",
            "lastname": "flores"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
    return response.json()


@pytest.fixture
def get_body_of_create_a_customer_with_full_information(get_token_login):
    token = get_token_login
    url = Singleton.get_base_url() + "/rest/default/V1/customers"
    random_alphanumeric_value = Singleton.get_random_alphanumeric(4)
    payload = json.dumps({
        "customer": {
            "group_id": 1,
            "default_billing": "2024-04-07 23:49:59",
            "default_shipping": "2024-04-07 23:49:59",
            "created_at": "2024-04-07 23:49:59",
            "updated_at": "2024-04-07 23:49:59",
            "created_in": "Default Store View",
            "dob": "2024-04-17",
            "email": f"{random_alphanumeric_value}@gmail.com",
            "firstname": f"{random_alphanumeric_value}_FN",
            "lastname": f"{random_alphanumeric_value}_LN",
            "middlename": f"{random_alphanumeric_value}_MN",
            "prefix": f"{random_alphanumeric_value}_P",
            "suffix": f"{random_alphanumeric_value}_S",
            "gender": 1,
            "store_id": 1,
            "website_id": 1,
            "addresses": [],
            "disable_auto_group_change": 0},
        "password": f"{Singleton.get_password()}!!",
        "redirectUrl": "string"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
    return response.json()


@pytest.fixture
def get_body_of_obtain_customer_group_by_id(get_token_login, group_id=1):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"
    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.get(url, headers=headers, data=payload)

    return response.json()