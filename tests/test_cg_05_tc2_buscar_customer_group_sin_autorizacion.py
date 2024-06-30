import pytest
import requests

from src.singleton import Singleton


@pytest.mark.functional
def test_CG_05_TC2_GET_verificar_respuesta_de_error_cuando_no_tienes_autorizacion():
    token = Singleton.get_token_no_valid()
    url = f"{Singleton.get_base_url()}/rest/V1/customerGroups/search?searchCriteria[currentPage]=1&searchCriteria[pageSize]=10"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 401
    assert response_data["message"] == "The consumer isn't authorized to access %resources."
    assert response_data["parameters"]["resources"] == "Magento_Customer::group"