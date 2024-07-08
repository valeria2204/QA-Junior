import pytest
from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.customer_group.setup import send_request_of_update_customer_group, setup_module
from src.enums.static_data import StaticData
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC1_PUT_verificar_status_code_200_cuando_se_actualiza_customer_group_con_datos_validos(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(8), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC2_PUT_validar_esquema_status_code_200_cuando_se_actualiza_customer_group_con_datos_validos(setup_module):
    response_json = send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(8), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(response_json, 'put_customer_group.json')

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC3_PUT_verificar_status_code_404_cuando_se_actualiza_customer_group_con_id_invalido(setup_module):
    send_request_of_update_customer_group(Utils.get_random_numerics(10), Utils.get_random_letters(8), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC4_PUT_validar_esquema_status_code_404_cuando_se_actualiza_customer_group_con_id_invalido(setup_module):
    response_json = send_request_of_update_customer_group(Utils.get_random_numerics(10), Utils.get_random_letters(8), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 404)
    assert_schemas(response_json, 'put_customer_group.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC5_PUT_verificar_status_code_401_cuando_se_actualiza_customer_group_sin_token_de_autenticacion(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(8), StaticData.tax_class_id.value, TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC6_PUT_validar_esquema_status_code_401_cuando_se_actualiza_customer_group_sin_token_de_autenticacion(setup_module):
    response_json = send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(8), StaticData.tax_class_id.value, TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)
    assert_schemas(response_json, 'put_customer_group.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC7_PUT_verificar_status_code_400_cuando_se_actualiza_customer_group_sin_proporcionar_code(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], StaticData.empty_name.value, StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC8_PUT_verificar_status_code_200_cuando_se_actualiza_customer_group_con_el_code_tiene_maximo_32_caracteres(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(35), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC9_PUT_verificar_status_code_400_cuando_se_actualiza_customer_con_tax_class_id_vacio(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(8), StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC10_PUT_verificar_status_code_200_cuando_se_actualiza_customer_con_solo_valores_numericos_en_code(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_numerics(8), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC11_PUT_verificar_status_code_400_cuando_se_actualiza_customer_con_solo_valores_alfabeticos_en_tax_class_id(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_letters(8), Utils.get_random_numerics(8))
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC12_PUT_verificar_status_code_400_cuando_se_actualiza_customer_con_solo_valores_alfabeticos_en_group_id(setup_module):
    send_request_of_update_customer_group(Utils.get_random_letters(8), Utils.get_random_letters(8), StaticData.tax_class_id.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG7TC13_PUT_verificar_status_code_200_cuando_se_actualiza_customer_con_solo_caracteres_en_tax_class_id(setup_module):
    send_request_of_update_customer_group(TestData.module_response_json["id"], Utils.get_random_numerics(8), Utils.get_random_symbols(5))
    assert_response_status(TestData.response_status_code, 400)
