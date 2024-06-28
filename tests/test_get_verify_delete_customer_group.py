import pytest
import requests

from src.singleton import Singleton


@pytest.mark.smoke
def test_CG9TC1_GET_verificar_si_un_customer_group_no_asignado_un_customer_puede_ser_eliminado(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/0/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 200
    assert str(response_data) is "True"


@pytest.mark.smoke
def test_CG9TC2_GET_verificar_si_un_customer_group_puede_ser_eliminado_por_un_id_no_existente(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1000/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 404
    assert str(response_data["message"]) == 'No such entity with %fieldName = %fieldValue'
    assert str(response_data["parameters"]["fieldName"]) == "groupId"
    assert str(response_data["parameters"]["fieldValue"]) == "1000"
