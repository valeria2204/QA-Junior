import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import send_request_of_delete_customer_group_by_id
from tests.conftest import setup_data
#assert_response_status,
 #   assert_response_schema,


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC1_DELETE_verificar_la_eliminacion_de_un_customer_group_con_id_valido(setup_data):
    group_id = "3"#cambiar id a uno que exista se elimina una ves pasa la prueba
    send_request_of_delete_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC2_DELETE_verificar_la_eliminacion_de_un_customer_group_con_id_de_un_grupo_prederterminado(setup_data):
    group_id = "1"
    send_request_of_delete_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC3_DELETE_verificar_la_eliminacion_de_un_customer_group_sin_token_de_autenticacion_con_id_valido(setup_data):
    group_id = "4"
    send_request_of_delete_customer_group_by_id(group_id, token="")
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC4_DELETE_verificar_la_eliminacion_de_un_customer_group_que_no_existe(setup_data):
    group_id = "999"
    send_request_of_delete_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
def test_CG8TC5_DELETE_verificar_status_code_OK_de_un_customer_group_utilizando_metodo_GET_en_lugar_de_DELETE(setup_data):
    group_id = "1"
    send_request_of_delete_customer_group_by_id(group_id, method="GET")
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.functional
def test_CG8TC6_DELETE_verificar_la_eliminacion_de_un_customer_group_introduciendo_texto_en_lugar_de_id(setup_data):
    group_id = "prueba"
    send_request_of_delete_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG8TC7_DELETE_verificar_la_eliminacion_de_un_customer_group_con_simbolos_en_lugar_de_id(setup_data):
    group_id = "!@#$%^&*"
    send_request_of_delete_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG8TC8_DELETE_verificar_la_eliminacion_de_un_customer_group_con_id_vacio(setup_data):
    group_id = ""
    send_request_of_delete_customer_group_by_id(group_id)
    assert_response_status(TestData.response_status_code, 404)



