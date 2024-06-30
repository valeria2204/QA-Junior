import json
import requests

from src.assertions.login_assertion import assert_login_success, assert_login_fail
from src.singleton import Singleton


def test_login_authentication():
    url = Singleton.get_base_url() + "/rest/default/V1/integration/admin/token"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({
        "username": Singleton.get_username(),
        "password": Singleton.get_password()
    })
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 200
    assert assert_login_success(response_data)

def test_login_authentication_fail():
    url = Singleton.get_base_url() + "/rest/default/V1/integration/admin/token"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({
        "username": Singleton.get_username(),
        "password": "Password falso"
    })
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 401
    assert assert_login_fail(response_data)
