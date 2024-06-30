import pytest
import requests
from src.singleton import Singleton
from src.assertions import Assertions


@pytest.mark.smoke
def test_CG04_TC1_GET_prueba_id_tienda_valido(get_token_login):
    token = get_token_login
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200


@pytest.mark.smoke
def test_CG04_TC2_GET_prueba_id_tienda_invalido(get_token_login):
    token = get_token_login
    store_id = 'invalid'
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400


@pytest.mark.smoke
def test_CG04_TC3_GET_prueba_sin_token_autenticacion():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_no_valid()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 401


@pytest.mark.functional
def test_CG04_TC4_GET_prueba_respuesta_id_tienda_valido(get_token_login):
    token = get_token_login
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    json_response = Assertions.assert_json_response(response)
    Assertions.assert_json_structure(json_response)


@pytest.mark.functional
def test_CG04_TC5_GET_prueba_error_id_tienda_invalido(get_token_login):
    token = get_token_login
    store_id = 'invalid'
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400


@pytest.mark.functional
def test_CG04_TC6_GET_prueba_error_sin_token_autenticacion():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_no_valid()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 401


@pytest.mark.functional
def test_CG04_TC7_GET_prueba_estructura_json_id_tienda_valido(get_token_login):
    token = get_token_login
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    json_response = Assertions.assert_json_response(response)
    Assertions.assert_json_structure(json_response)


@pytest.mark.functional
def test_CG04_TC8_GET_prueba_manejo_id_tienda_ausente(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200


@pytest.mark.regression
def test_CG04_TC9_GET_prueba_consistencia_id_tienda_valido(get_token_login):
    token = get_token_login
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200


@pytest.mark.regression
def test_CG04_TC10_GET_prueba_consistencia_id_tienda_invalido(get_token_login):
    token = get_token_login
    store_id = 'invalid'
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400


@pytest.mark.regression
def test_CG04_TC11_GET_prueba_consistencia_sin_token_autenticacion():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_no_valid()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 401


@pytest.mark.regression
def test_CG04_TC12_GET_prueba_estructura_json_id_tienda_valido_regresion(get_token_login):
    token = get_token_login
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    json_response = Assertions.assert_json_response(response)
    Assertions.assert_json_structure(json_response)


@pytest.mark.regression
def test_CG04_TC13_GET_prueba_manejo_id_tienda_post_actualizacion(get_token_login):
    token = get_token_login
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
