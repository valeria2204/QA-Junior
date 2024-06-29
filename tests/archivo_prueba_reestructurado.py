import requests
import pytest
from src.singleton import Singleton
from tests.assertions import assert_unauthorized_response

@pytest.mark.functional
def test_CG_05_TC2_GET_verificar_error_con_bearer_token_no_valido():
    token = Singleton.get_token_no_valid()
    url = f"{Singleton.get_base_url()}/rest/V1/customerGroups/search?searchCriteria[currentPage]=1&searchCriteria[pageSize]=10"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert_unauthorized_response(response)
