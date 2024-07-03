import pytest
import requests

from src.assertions.assertions_schema import assert_schemas
from src.assertions.assertions import assert_response_status
from src.enums.uri import URIComplement
from src.headers.headers import header_authorization
from src.testdata import TestData
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC1_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido(setup_data):
    store_id = "1"
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token_all_access)
    response = requests.request("GET", url, headers=headers)

    assert_response_status(response.status_code,200)


@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC2_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_invalido(setup_data):
    store_id = 'invalid'
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token)
    response = requests.request("GET", url, headers=headers)

    assert_response_status(response.status_code,400)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG04_TC3_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_sin_token_de_autenticacion(setup_data):
    store_id = "1"
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token_no_valid)
    response = requests.request("GET", url, headers=headers)

    assert_response_status(response.status_code,401)



@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC4_GET_verificar_esquema_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido(setup_data):
    store_id = "1"
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token)
    response = requests.request("GET", url, headers=headers)

    assert_response_status(response.status_code,200)
    assert_schemas(response.json(), "get_customer_group.json")



@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC5_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_vacio(setup_data):
    store_id = ""
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token_all_access)
    response = requests.request("GET", url, headers=headers)

    assert_response_status(response.status_code,200)


@pytest.mark.regression
def test_CG04_TC6_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_post(setup_data):
    store_id = "1"
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token_all_access)
    response = requests.request("POST", url, headers=headers)

    assert_response_status(response.status_code,404)


@pytest.mark.regression
def test_CG04_TC7_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_put(setup_data):
    store_id = "1"
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token_all_access)
    response = requests.request("PUT", url, headers=headers)

    assert_response_status(response.status_code, 404)


@pytest.mark.regression
def test_CG04_TC8_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_delete():
    store_id = "1"
    url = f"{TestData.base_url}{URIComplement.GET_CUSTOMER_GROUP_BY_STORE_ID.value}".replace(URIComplement.STORE_ID_KEY_NAME.value, store_id)

    headers = header_authorization(TestData.token_all_access)
    response = requests.request("DELETE", url, headers=headers)

    assert_response_status(response.status_code,404)