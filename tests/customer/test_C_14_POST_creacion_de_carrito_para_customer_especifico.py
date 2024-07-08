import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.assertions.assertions_schema import assert_schemas
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.customer.setup import setup_module, setup_module_full_customer, send_request_for_assign_a_new_cart_to_a_customer, setup_function
from tests.helpers.utils import Utils
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC1_POST_verificar_status_code_200_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_nuevo_creado_con_requerimientos_minimos(setup_module):
    send_request_for_assign_a_new_cart_to_a_customer(TestData.module_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC2_POST_verificar_status_code_200_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_nuevo_creado_con_todos_los_valores_llenados(setup_module_full_customer):
    send_request_for_assign_a_new_cart_to_a_customer(TestData.module_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC3_POST_verificar_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_invalido_de_tipo_simbolo(setup_module):
    customer_id = StaticData.symbols.value
    send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC4_POST_verificar_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_invalido_de_tipo_letra(setup_module):
    customer_id = Utils.get_random_letters(2)
    send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC5_POST_verificar_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_vacio(setup_module):
    customer_id = StaticData.empty_name.value
    send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC6_POST_verificar_status_code_404_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_no_existente(setup_module):
    customer_id = Utils.get_random_numerics(10)
    send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
@pytest.mark.regression
def test_C14TC7_POST_verificar_status_code_401_cuando_se_asigna_un_carrito_a_un_customer_sin_token_de_autorizacion(setup_function):
    send_request_for_assign_a_new_cart_to_a_customer(TestData.function_response_json["id"], TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.functional
@pytest.mark.regression
def test_C14TC8_POST_validar_esquema_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_invalido_de_tipo_simbolo(setup_module):
    customer_id = StaticData.symbols.value
    response = send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_schemas(response, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C14TC9_POST_validar_esquema_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_invalido_de_tipo_letra(setup_module):
    customer_id = Utils.get_random_letters(2)
    response = send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_schemas(response, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C14TC10_POST_validar_esquema_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_vacio(setup_module):
    customer_id = StaticData.empty_name.value
    response = send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_schemas(response, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C14TC11_POST_validar_esquema_status_code_400_cuando_se_asigna_un_carrito_a_un_customer_con_un_customer_id_no_existente(setup_module):
    customer_id = Utils.get_random_numerics(10)
    response = send_request_for_assign_a_new_cart_to_a_customer(customer_id)
    assert_schemas(response, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C14TC12_POST_validar_esquema_status_code_401_cuando_se_asigna_un_carrito_a_un_customer_sin_token_de_autorizacion(setup_function):
    response = send_request_for_assign_a_new_cart_to_a_customer(TestData.function_response_json["id"], TestData.token_no_valid)
    assert_schemas(response, SchemaName.response_status_401_unauthorized.value)