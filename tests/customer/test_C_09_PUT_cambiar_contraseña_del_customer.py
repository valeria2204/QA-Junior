import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData

from tests.customer.setup import send_request_of_update_password_of_a_customer, setup_function_customer_with_account
from tests.helpers.utils import Utils
from src.enums.static_data import StaticData


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC1_PUT_verificar_status_code_400_cuando_se_cambia_password_de_customer_con_el_nuevo_password_es_tipo_alfabetico(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_letters(12), StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC2_PUT_validar_esquema_status_code_400_cuando_se_cambia_password_de_customer_con_un_nuevo_password_de_tipo_alfabetico(
        setup_function_customer_with_account):
    response_json = send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_letters(12), StaticData.password.value)
    assert_schemas(response_json, 'put_new_password_to_customer.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC3_PUT_verificar_status_code_401_cuando_el_cambio_de_password_para_el_parametro_old_passsword_no_es_valido(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_password(12), old_password=Utils.get_random_letters(12))
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC4_PUT_validar_esquema_status_code_401_cuando_el_cambio_de_password_para_el_parametro_old_password_no_es_valido(
        setup_function_customer_with_account):
    response_json = send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_password(12), old_password=Utils.get_random_letters(12))
    assert_schemas(response_json, 'put_new_password_to_customer.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC5_PUT_verificar_status_code_200_cuando_el_cambio_de_password_de_customer_con_un_parametro_new_password_tiene_mas_de_256_caracteres(
        setup_function_customer_with_account):
    new_password = Utils.get_random_password(260)
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], new_password, StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.xfail(raises=RuntimeError)
def test_C9TC6_PUT_verificar_status_code_401_cuando_el_cambio_de_password_de_customer_con_el_parametro_old_password_vacio(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_password(12), old_password=StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC7_PUT_verificar_status_code_400_cuando_el_cambio_de_password_de_customer_con_el_parametro_new_password_vacio(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], "", StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC8_PUT_verificar_status_code_400_cuando_el_cambio_de_password_de_customer_con_el_parametro_new_password_tiene_caracteres_invalidos(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], "?", StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC9_PUT_verificar_status_code_400_cuando_el_cambio_de_password_de_customer_con_el_parametro_new_password_es_de_tipo_numericos(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_numerics(12), StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC10_PUT_verificar_status_code_400_cuando_el_cambio_de_password_de_customer_con_el_parametro_new_password_no_contiene_valores_tipo_numericos(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], "Demos#", StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC11_PUT_verificar_status_code_400_cuando_el_cambio_de_password_de_customer_con_un_parametro_new_password_tiene_menos_de_8_caracteres(
        setup_function_customer_with_account):
    new_password = Utils.get_random_password(7)
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], new_password, StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC12_PUT_verificar_status_code_400_cuando_cuando_se_cambia_password_de_customer_con_el_id_incorrecto(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(StaticData.empty_name, Utils.get_random_password(12), StaticData.password.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C9TC13_PUT_verificar_status_code_200_cuando_se_cambia_password_de_customer_con_valores_validos(
        setup_function_customer_with_account):
    send_request_of_update_password_of_a_customer(TestData.function_response_json_customer["id"], Utils.get_random_password(12), StaticData.password.value)
    assert_response_status(TestData.response_status_code, 200)
