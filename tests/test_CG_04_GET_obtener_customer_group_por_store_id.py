import pytest
import requests

from src.assertions.assertions_schema import assert_schemas
from src.assertions.assertions import assert_response_status
from src.singleton import Singleton


@pytest.mark.smoke
def test_CG04_TC1_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_all_access()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert_response_status(response.status_code,200)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG04_TC2_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_invalido(get_token_login):
    token = get_token_login
    store_id = 'invalid'
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers)
    assert_response_status(response.status_code,400)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG04_TC3_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_sin_token_de_autenticacion():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_no_valid()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert_response_status(response.status_code,401)


@pytest.mark.functional
def test_CG04_TC4_GET_verificar_esquema_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_all_access()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert_response_status(response.status_code,200)
    assert_schemas(response.json(), "get_customer_group.json")


@pytest.mark.functional
def test_CG04_TC5_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_vacio():
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_all_access()}',
    }

    response = requests.request("GET", url, headers=headers)
    assert_response_status(response.status_code,200)


@pytest.mark.regression
def test_CG04_TC6_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_post():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_all_access()}',
    }

    response = requests.request("POST", url, headers=headers)
    assert_response_status(response.status_code,404)


@pytest.mark.regression
def test_CG04_TC7_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_put():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_all_access()}',
    }

    response = requests.request("PUT", url, headers=headers)
    assert_response_status(response.status_code,404)
#bug se espera codigo 404 pero devuelve 200 cuando obtenemos del customer group por defecto con storeId valido cuando se usa el metodo put

@pytest.mark.regression
def test_CG04_TC8_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_delete():
    store_id = 1
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default/{store_id}"

    headers = {
        'Authorization': f'Bearer {Singleton.get_token_all_access()}',
    }

    response = requests.request("DELETE", url, headers=headers)
    assert_response_status(response.status_code,404)