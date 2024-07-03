import pytest
import requests

from src.assertions.assertions_schema import assert_schemas
from src.assertions.assertions import assert_response_status
from src.enums.method import Method
from src.enums.uri import URIComplement
from src.headers.headers import header_authorization
from src.testdata import TestData
from tests.conftest import setup_data, send_request_of_obtain_default_customer_group_by_store_id


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC1_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido(setup_data):
    store_id = "1"
    send_request_of_obtain_default_customer_group_by_store_id(store_id, TestData.token_all_access)

    assert_response_status(TestData.response_status_code,200)


@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC2_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_invalido(setup_data):
    store_id = 'invalid'
    send_request_of_obtain_default_customer_group_by_store_id(store_id)

    assert_response_status(TestData.response_status_code,400)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG04_TC3_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_sin_token_de_autenticacion(setup_data):
    store_id = "1"
    send_request_of_obtain_default_customer_group_by_store_id(store_id, TestData.token_no_valid)

    assert_response_status(TestData.response_status_code,401)



@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC4_GET_verificar_esquema_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido(setup_data):
    store_id = "1"
    send_request_of_obtain_default_customer_group_by_store_id(store_id)

    assert_schemas(TestData.response_json, "get_customer_group.json")



@pytest.mark.functional
@pytest.mark.regression
def test_CG04_TC5_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_vacio(setup_data):
    store_id = ""
    send_request_of_obtain_default_customer_group_by_store_id(store_id, TestData.token_all_access)

    assert_response_status(TestData.response_status_code,200)


@pytest.mark.regression
def test_CG04_TC6_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_post(setup_data):
    store_id = "1"
    send_request_of_obtain_default_customer_group_by_store_id(store_id, TestData.token_all_access, Method.POST.value)

    assert_response_status(TestData.response_status_code,404)


@pytest.mark.regression
def test_CG04_TC7_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_put(setup_data):
    store_id = "1"
    send_request_of_obtain_default_customer_group_by_store_id(store_id, TestData.token_all_access, Method.PUT.value)

    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG04_TC8_GET_verificar_la_obtencion_del_customer_group_por_defecto_con_storeId_valido_cuando_se_usa_el_metodo_delete():
    store_id = "1"
    send_request_of_obtain_default_customer_group_by_store_id(store_id, TestData.token_all_access, Method.DELETE.value)

    assert_response_status(TestData.response_status_code, 404)