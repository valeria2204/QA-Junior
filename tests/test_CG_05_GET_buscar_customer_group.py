import pytest
import requests
import jsonschema

from src.singleton import Singleton


@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC4_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_POST(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    payload = {}

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    assert response.status_code == 404, "NO FOUND 404"


@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC5_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_PUT(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    payload = {}

    response = requests.put(url, headers=headers, json=payload)
    response_data = response.json()

    assert response.status_code == 400, "NO FOUND 400"


@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC6_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_DELETE(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    payload = {}

    response = requests.delete(url, headers=headers, json=payload)
    response_data = response.json()

    assert response.status_code == 400, "NO FOUND 400"

def test_schema_verificar_obtencion_exitosa_de_los_customer_groups(get_body_obtain_first_10_customer_groups):
    response_data = get_body_obtain_first_10_customer_groups
    schema = Singleton.read_schema_json_file('get_obtain_first_10_customer_groups.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC11_GET_verificar_que_el_primer_customer_group_es_encontrado_por_los_criterios_de_busqueda_field_value_condition_type(get_token_login):
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
def test_CG05TC3_GET_verificar_que_ningun_customer_group_es_encontrado_con_los_valores_invalidos_para_los_criterios_de_busqueda_field_value_condition_type(get_token_login):
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
def test_CG05TC2_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_groups_cuando_no_tienes_autorizacion():
    token = Singleton.get_token_no_valid()
    url = f"{Singleton.get_base_url()}/rest/V1/customerGroups/search?searchCriteria[currentPage]=1&searchCriteria[pageSize]=10"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 401, "Unauthorized"
