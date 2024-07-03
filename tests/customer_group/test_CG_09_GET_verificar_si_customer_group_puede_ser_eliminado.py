import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import send_request_of_check_if_customer_group_can_be_deleted_with_group_id
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC1_GET_verificar_si_un_customer_group_no_asignado_a_un_customer_puede_ser_eliminado(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("0", "GET", TestData.token)
    assert_response_status(TestData.response_status_code, 200)
    assert TestData.response_json is True


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC2_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_no_existente(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1000", "GET", TestData.token)
    assert_response_status(TestData.response_status_code, 404)
    assert TestData.response_json["parameters"]["fieldValue"] == 1000


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC3_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_vacio(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("", "GET", TestData.token)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC4_GET_verificar_si_un_customer_group_asignado_a_un_customer_puede_ser_eliminado(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("2", "GET", TestData.token)
    assert_response_status(TestData.response_status_code, 200)
    assert str(TestData.response_json) is "False"


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC5_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_tipo_texto(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("sss", "GET", TestData.token)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC6_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_caracter_especial(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("$$$$", "GET", TestData.token)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC7_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_token_no_tiene_permisos(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("0", "GET", TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.regression
def test_CG9TC12_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "POST", TestData.token)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG9TC13_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "PUT", TestData.token)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG9TC14_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "DELETE", TestData.token)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC8_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_no_existente(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1000", "GET", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_404_no_such_entity.json')
    assert TestData.response_json["message"] == 'No such entity with %fieldName = %fieldValue'
    assert TestData.response_json["parameters"]["fieldName"] == "groupId"


@pytest.mark.regression
def test_CG9TC9_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_vacio(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("", "GET", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_400_type_value_is_invalid.json')
    assert TestData.response_status_code == 400
    assert TestData.response_json["message"] == "The \"\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.regression
def test_CG9TC10_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_tipo_texto(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("texto", "GET", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_400_type_value_is_invalid.json')
    assert TestData.response_status_code == 400
    assert TestData.response_json["message"] == "The \"texto\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.regression
def test_CG9TC11_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_caracter_especial(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("$$$$$", "GET", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_400_type_value_is_invalid.json')
    assert TestData.response_status_code == 400
    assert TestData.response_json["message"] == "The \"$$$$$\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.regression
def test_CG9TC15_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_token_no_tiene_permisos(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "GET", TestData.token_no_valid)
    assert_schemas(TestData.response_json, 'response_status_code_400_type_value_is_invalid.json')
    assert TestData.response_status_code == 401
    assert TestData.response_json["message"] == "The consumer isn't authorized to access %resources."
    assert TestData.response_json["parameters"]["resources"] == "Magento_Customer::group"


@pytest.mark.regression
def test_CG9TC16_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "POST", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_404_request_does_not_match.json')
    assert TestData.response_json["message"] == "Request does not match any route."


@pytest.mark.regression
def test_CG9TC17_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "PUT", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_404_request_does_not_match.json')
    assert TestData.response_json["message"] == "Request does not match any route."


@pytest.mark.regression
def test_CG9TC18_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id("1", "DELETE", TestData.token)
    assert_schemas(TestData.response_json, 'response_status_code_404_request_does_not_match.json')
    assert TestData.response_json["message"] == "Request does not match any route."

