import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.assertions.assertions_schema import assert_schemas
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.customer.setup import setup_function, send_request_of_remove_customer, setup_function_full_customer
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC1_DELETE_verificar_status_code_200_al_eliminar_un_customer_nuevo(setup_function):
    send_request_of_remove_customer(TestData.function_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC2_DELETE_verificar_status_code_400_al_eliminar_un_customer_con_customer_id_invalido_de_tipo_simbolo(setup_function):
    customer_id = Utils.get_random_symbols(5)
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC3_DELETE_verificar_status_code_400_al_eliminar_un_customer_con_customer_id_invalido_de_tipo_letra(setup_function):
    customer_id = Utils.get_random_letters(2)
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC4_DELETE_verificar_status_code_404_al_eliminar_un_customer_con_customer_id_vacio(setup_function):
    customer_id = StaticData.empty_name.value
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC5_DELETE_verificar_status_code_404_al_eliminar_un_customer_con_customer_id_no_existente(setup_function):
    customer_id = Utils.get_random_numerics(10)
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC6_DELETE_verificar_status_code_200_al_eliminar_un_customer_con_los_requerimientos_minimos(setup_function):
    send_request_of_remove_customer(TestData.function_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC7_DELETE_verificar_status_code_200_al_eliminar_un_customer_con_todos_los_valores_llenados(setup_function_full_customer):
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.functional
@pytest.mark.regression
def test_CG6TC8_GET_verificar_status_code_401_al_eliminar_un_customer_sin_token_de_autorizacion(setup_function):
    send_request_of_remove_customer(TestData.function_response_json["id"], TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC9_DELETE_validar_respuesta_true_al_eliminar_un_customer_nuevo(setup_function):
    response = send_request_of_remove_customer(TestData.function_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)
    assert_equals(response, True)


@pytest.mark.functional
@pytest.mark.regression
def test_C5TC10_DELETE_Validar_esquema_status_code_400_al_eliminar_un_customer_con_customer_id_invalido_de_tipo_simbolo(setup_function):
    customer_id = Utils.get_random_symbols(5)
    response = send_request_of_remove_customer(customer_id)
    assert_schemas(response, SchemaName.response_status_code_400_type_value_is_invalid.value)


#def test_C5TC11_DELETE_validar_esquema_status_code_400_al_eliminar_un_customer_con_customer_id_invalido_de_tipo_letra(setup_function):

@pytest.mark.functional
@pytest.mark.regression
def test_C5TC_DELETE_validar_esquema_status_code_400_al_eliminar_un_customer_nuevo(setup_function):
    customer_id = Utils.get_random_numerics(10)
    response = send_request_of_remove_customer(customer_id)
    assert_schemas(response, SchemaName.response_status_code_400_type_value_is_invalid.value)
