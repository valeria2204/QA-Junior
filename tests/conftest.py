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
def get_body_create_customer(get_token_login):
    token = get_token_login
    url = Singleton.get_base_url() + "/rest/default/V1/customers"
    payload = json.dumps({
        "customer": {
            "email": f"{Singleton.get_random_string(4)}@gmail.com",
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
def get_body_customer_group(get_token_login):
    token = get_token_login
    url = Singleton.get_base_url() + "/rest/default/V1/customerGroups/default/"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    return response.json()