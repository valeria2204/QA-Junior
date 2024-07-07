import json
import pytest

from src.enums.method import Method
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type
from src.testdata import TestData


@pytest.fixture(scope="session")
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
    response = TestData.request_client(Method.POST.value, url, headers, payload).run()
    return response.json()

