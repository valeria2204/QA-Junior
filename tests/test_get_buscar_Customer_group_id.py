import pytest
import requests

from src.singleton import Singleton


@pytest.mark.smoke
def test_CG_05_GET_TC11_verificar_respuesta_exitosa(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    params = {
        'searchCriteria[filterGroups][0][filters][0][field]': 'id',
        'searchCriteria[filterGroups][0][filters][0][value]': '1',
        'searchCriteria[filterGroups][0][filters][0][condition_type]': 'eq'
    }

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()

    assert response.status_code == 200, "Expected status code 200"


@pytest.mark.smoke
def test_CG_05_GET_TC3_verificar_comportamiento_con_parametros_invalidos(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    params = {
        'searchCriteria[filterGroups][0][filters][0][field]': 'nonexistent_field',
        'searchCriteria[filterGroups][0][filters][0][value]': 'invalid_value',
        'searchCriteria[filterGroups][0][filters][0][condition_type]': 'invalid_condition'
    }

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()

    assert response.status_code == 500, "Internal Server Error"


@pytest.mark.regression
def test_CG_05_GET_TC7_verificar_mensaje_de_exito(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    params = {
        'searchCriteria[filterGroups][0][filters][0][field]': 'id',
        'searchCriteria[filterGroups][0][filters][0][value]': '1',
        'searchCriteria[filterGroups][0][filters][0][condition_type]': 'eq'
    }

    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()

    assert response.status_code == 200, "Expected status code 200"
