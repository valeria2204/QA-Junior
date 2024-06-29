import json
import requests

from src.singleton import Singleton
from assertions import login_assertions

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
    assert response_data is not None

    # Llama a la función que contiene las assertions
    login_assertions(response)