import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.assertions.assertions_schema import assert_schemas
from src.enums.method import Method
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer_group.setup import send_request_of_check_if_customer_group_can_be_deleted_with_group_id, setup_function_customer_group
from tests.customer.setup import send_request_of_update_a_customer, setup_function_customer
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC1_GET_verificar_si_un_customer_group_predeterminado_no_puede_ser_eliminado(
        setup_function_customer_group):
    response = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.GET.value, TestData.token)
    assert_response_status(TestData.response_status_code, 200)
    assert_equals(response, True)


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC2_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_no_existente(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.non_existing_id.value)
    assert_response_status(TestData.response_status_code, 404)
    assert_equals(response_json["parameters"]["fieldValue"], StaticData.non_existing_id.value)


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC3_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_vacio(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC4_GET_verificar_si_un_customer_group_asignado_a_un_customer_puede_ser_eliminado(
        setup_function_customer_group, setup_function_customer):
    TestData.function_response_json_customer[StaticData.group_id.name] = TestData.function_response_json_customer_group["id"]
    send_request_of_update_a_customer(TestData.function_response_json_customer["id"], TestData.function_response_json_customer)
    response = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(TestData.function_response_json_customer_group["id"])
    assert_response_status(TestData.response_status_code, 200)
    assert_equals(response, False)


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC5_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_tipo_texto(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(Utils.get_random_letters(5))
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC6_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_caracter_especial(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.symbols.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC7_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_token_no_tiene_permisos(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.GET.value, TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.regression
def test_CG9TC12_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.POST.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG9TC13_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.PUT.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG9TC14_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(setup_data):
    send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.DELETE.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG9TC8_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_no_existente(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.non_existing_id.value)
    assert_schemas(response_json, SchemaName.response_status_code_404_no_such_entity.value)
    assert_equals(response_json["message"], StaticData.no_such_entity_with_fieldName_equal_fieldValue.value)


@pytest.mark.regression
def test_CG9TC9_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_vacio(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.empty_name.value)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_equals(response_json["message"], StaticData.the_values_type_is_invalid.value.replace(StaticData.value.value, StaticData.empty_name.value))


@pytest.mark.regression
def test_CG9TC10_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_tipo_texto(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.firstname.value)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.response_status_code, 400)
    assert_equals(response_json["message"], StaticData.the_values_type_is_invalid.value.replace(StaticData.value.value, StaticData.firstname.value))


@pytest.mark.regression
def test_CG9TC11_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_caracter_especial(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.symbols.value)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_equals(response_json["message"], StaticData.the_values_type_is_invalid.value.replace(StaticData.value.value, StaticData.symbols.value))


@pytest.mark.regression
def test_CG9TC15_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_token_no_tiene_permisos(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.GET.value, TestData.token_no_valid)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_response_status(TestData.response_status_code, 401)
    assert_equals(response_json["message"], StaticData.the_consumer_isnt_authorized_to_access_resources.value)


@pytest.mark.regression
def test_CG9TC16_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.POST.value)
    assert_schemas(response_json, SchemaName.response_status_code_404_request_does_not_match.value)
    assert_equals(response_json["message"], StaticData.request_does_not_match_any_route.value)


@pytest.mark.regression
def test_CG9TC17_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.PUT.value)
    assert_schemas(response_json, SchemaName.response_status_code_404_request_does_not_match.value)
    assert_equals(response_json["message"], StaticData.request_does_not_match_any_route.value)


@pytest.mark.regression
def test_CG9TC18_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(setup_data):
    response_json = send_request_of_check_if_customer_group_can_be_deleted_with_group_id(StaticData.group_id.value, Method.DELETE.value)
    assert_schemas(response_json, SchemaName.response_status_code_404_request_does_not_match.value)
    assert_equals(response_json["message"], StaticData.request_does_not_match_any_route.value)

