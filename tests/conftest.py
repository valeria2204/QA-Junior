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
def get_body_obtain_first_10_customer_groups(get_token_login):
    token = get_token_login
    url = Singleton.get_base_url() + "/rest/V1/customerGroups/search?searchCriteria[currentPage]=1&searchCriteria[pageSize]=10"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

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
