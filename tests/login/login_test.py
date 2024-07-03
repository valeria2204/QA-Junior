import json
import requests

from src.enums.uri import URIComplement
from src.testdata import TestData
from tests.conftest import setup_data


def test_login_authentication(setup_data):
    url = f"{TestData.base_url}{URIComplement.POST_GET_TOKEN.value}"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({
        "username": TestData.username,
        "password": TestData.password
    })
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data is not None
