import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import send_request_of_obtain_customer_group_by_id
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC1_GET_verificar_obtencion_exitosa_de_customer_group_por_id(setup_data):
    group_id = "1"
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 200)

    
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC2_GET_validar_esquema_obtencion_exitosa_de_customer_group_por_id(setup_data):
    group_id = "1"
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_schemas(TestData.response_json, 'get_customer_group.json')

    
@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC3_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_alfabetico(setup_data):
    group_id = "ASD"
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC4_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_de_caracter_especial(setup_data):
    group_id = "@"
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC5_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_vacio(setup_data):
    group_id = ""
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC6_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_no_existente(setup_data):
    group_id = "52542542542"
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC7_GET_validar_error_de_no_autorizado_al_acceder_sin_token_de_autorizacion():
    group_id = "1"
    send_request_of_obtain_customer_group_by_id(group_id, TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)
