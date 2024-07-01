import pytest
import requests

from src.singleton import Singleton


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG_05_GET_TC11_GET_verificar_que_el_primer_customer_group_es_encontrado_por_los_criterios_de_busqueda_field_value_condition_type(get_token_login):
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
def test_CG_05_GET_TC3_verificar_que_ningun_customer_group_es_encontrado_con_los_valores_invalidos_para_los_criterios_de_busqueda_field_value_condition_type(get_token_login):
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

@pytest.mark.smoke
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

    assert response.status_code == 401, "Unauthorized"
