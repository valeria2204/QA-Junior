import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer_group.setup import setup_module, send_request_of_obtain_customer_group_by_id
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC1_GET_verificar_obtencion_exitosa_de_customer_group_por_id(setup_module):
    send_request_of_obtain_customer_group_by_id(TestData.module_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)

    
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC2_GET_validar_esquema_obtencion_exitosa_de_customer_group_por_id(setup_module):
    response_json = send_request_of_obtain_customer_group_by_id(TestData.module_response_json["id"])
    assert_schemas(response_json, SchemaName.get_customer_group.value)

    
@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC3_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_alfabetico(setup_data):
    group_id = Utils.get_random_letters(3)
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC4_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_de_caracter_especial(setup_data):
    group_id = StaticData.symbols.value
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC5_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_vacio(setup_data):
    group_id = StaticData.empty_name.value
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC6_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_no_existente(setup_data):
    group_id = Utils.get_random_numerics(10)
    send_request_of_obtain_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC7_GET_validar_error_de_no_autorizado_al_acceder_sin_token_de_autorizacion(setup_data):
    send_request_of_obtain_customer_group_by_id(StaticData.group_id.value, TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)
