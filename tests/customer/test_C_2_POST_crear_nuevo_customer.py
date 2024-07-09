import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.assertions.assertions_schema import assert_schemas
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.customer.setup import setup_module, send_request_of_create_a_customer, teardown_function_remove_customer
from tests.conftest import setup_data
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C2TC1_POST_verificar_status_code_200_cuando_se_crea_nueva_cuenta_customer_con_requerimientos_minimos(setup_module):
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C2TC2_POST_validar_esquema_verificar_status_code_200_cuando_se_crea_nueva_cuenta_customer_con_requerimientos_minimos(setup_module):
    assert_schemas(TestData.module_response_json, SchemaName.post_customer.value)
    assert_equals(TestData.module_response_json[StaticData.email.name], TestData.random_email)
    assert_equals(TestData.module_response_json[StaticData.firstname.name], StaticData.firstname.value)
    assert_equals(TestData.module_response_json[StaticData.lastname.name], StaticData.lastname.value)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C2TC3_POST_verificar_status_code_200_cuando_se_crea_nueva_cuenta_customer_con_todos_los_campos(teardown_function_remove_customer):
    random_email = Utils.get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(
        random_email,
        StaticData.firstname.value,
        StaticData.lastname.value,
        StaticData.group_id.value,
        StaticData.default_billing.value,
        StaticData.default_shipping.value,
        StaticData.created_at.value,
        None,
        StaticData.created_in.value,
        StaticData.dob.value,
        StaticData.middlename.value,
        StaticData.prefix.value,
        StaticData.suffix.value,
        StaticData.gender.value,
        StaticData.store_id.value,
        StaticData.website_id.value,
        StaticData.addresses.value,
        StaticData.disable_auto_group_change.value,
        StaticData.password.value,
        StaticData.redirectUrl.value
    )
    assert_response_status(TestData.response_status_code, 200)
    assert_equals(TestData.function_response_json[StaticData.email.name], random_email)
    assert_equals(TestData.function_response_json[StaticData.firstname.name], StaticData.firstname.value)
    assert_equals(TestData.function_response_json[StaticData.group_id.name], StaticData.group_id.value)
    assert_equals(TestData.function_response_json[StaticData.default_billing.name], StaticData.default_billing.value.split('-')[0])
    assert_equals(TestData.function_response_json[StaticData.default_shipping.name], StaticData.default_shipping.value.split('-')[0])
    assert_equals(TestData.function_response_json[StaticData.created_at.name], StaticData.created_at.value)
    assert_equals(TestData.function_response_json[StaticData.created_in.name], StaticData.created_in.value)
    assert_equals(TestData.function_response_json[StaticData.dob.name], StaticData.dob.value)
    assert_equals(TestData.function_response_json[StaticData.middlename.name], StaticData.middlename.value)
    assert_equals(TestData.function_response_json[StaticData.prefix.name], StaticData.prefix.value)
    assert_equals(TestData.function_response_json[StaticData.suffix.name], StaticData.suffix.value)
    assert_equals(TestData.function_response_json[f'{StaticData.gender=}'.split('=')[0].split('.')[1]], StaticData.gender.value)
    assert_equals(TestData.function_response_json[f'{StaticData.store_id=}'.split('=')[0].split('.')[1]], StaticData.store_id.value)
    assert_equals(TestData.function_response_json[f'{StaticData.website_id=}'.split('=')[0].split('.')[1]], StaticData.website_id.value)
    assert_equals(TestData.function_response_json[StaticData.addresses.name], StaticData.addresses.value)
    assert_equals(TestData.function_response_json[StaticData.disable_auto_group_change.name], StaticData.disable_auto_group_change.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC4_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valores_vacios_para_todos_los_req_vacios(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer("", "", "")
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], 'The customer email is missing. Enter and try again.')


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC5_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valor_vacio_para_email(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(StaticData.empty_name.value, StaticData.firstname.value, StaticData.lastname.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], 'The customer email is missing. Enter and try again.')


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC6_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valor_solo_texto_para_email(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(Utils.get_random_letters(10), StaticData.firstname.value, StaticData.lastname.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], '"Email" is not a valid email address.')


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC7_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valor_solo_numerico_para_email(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(Utils.get_random_numerics(10), StaticData.firstname.value, StaticData.lastname.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], '"Email" is not a valid email address.')


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC8_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valor_solo_simbolos_para_email(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(StaticData.symbols.value, StaticData.firstname.value, StaticData.lastname.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], '"Email" is not a valid email address.')


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC9_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valor_vacio_para_first_name(
        teardown_function_remove_customer):
    random_email = Utils().get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(random_email, StaticData.empty_name.value, StaticData.lastname.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], '"First Name" is a required value.')

@pytest.mark.functional
@pytest.mark.regression
def test_C2TC10_POST_verificar_status_code_400_cuando_se_crea_nueva_cuenta_customer_con_valor_vacio_para_last_name(
        teardown_function_remove_customer):
    random_email = Utils().get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(random_email, StaticData.firstname.value, StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], '"Last Name" is a required value.')


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC11_POST_verificar_crear_nueva_cuenta_customer_con_el_group_id_vacio(teardown_function_remove_customer):
    random_email = Utils.get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(
        random_email,
        StaticData.firstname.value,
        StaticData.lastname.value,
        StaticData.empty_name.value,
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], "Error occurred during \"group_id\" processing. The \"\" value's type is invalid. The \"int\" type was expected. Verify and try again.")


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC12_POST_verificar_crear_nueva_cuenta_customer_con_el_group_id_igual_a_texto(
        teardown_function_remove_customer):
    random_text = Utils.get_random_letters(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        random_text,
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], f"Error occurred during \"group_id\" processing. The \"{random_text}\" value's type is invalid. The \"int\" type was expected. Verify and try again.")


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC13_POST_verificar_crear_nueva_cuenta_customer_con_el_group_id_igual_a_simbolos(
        teardown_function_remove_customer):
    random_symbols = Utils.get_random_symbols(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        random_symbols,
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(TestData.function_response_json["message"], f"Error occurred during \"group_id\" processing. The \"{random_symbols}\" value's type is invalid. The \"int\" type was expected. Verify and try again.")


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC14_POST_verificar_crear_nueva_cuenta_customer_con_el_group_id_igual_a_un_id_inexistente(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        StaticData.non_existing_id.value
    )
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(TestData.function_response_json, SchemaName.post_customer.value)
    assert_equals(TestData.function_response_json["group_id"], StaticData.group_id.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC15_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_created_in_vacio(
        teardown_function_remove_customer):
    random_email = Utils.get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(
        random_email,
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        StaticData.empty_name.value
    )
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(TestData.function_response_json, SchemaName.post_customer.value)
    assert_equals(TestData.function_response_json[StaticData.created_in.name], StaticData.created_in.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC16_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_created_in_igual_a_texto(
        teardown_function_remove_customer):
    random_text = Utils.get_random_letters(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        random_text
    )
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(TestData.function_response_json, SchemaName.post_customer.value)
    assert_equals(TestData.function_response_json[StaticData.created_in.name], StaticData.created_in.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC17_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_created_in_igual_a_simbolos(
        teardown_function_remove_customer):
    random_symbols = Utils.get_random_symbols(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        random_symbols
    )
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(TestData.function_response_json, SchemaName.post_customer.value)
    assert_equals(TestData.function_response_json[StaticData.created_in.name], StaticData.created_in.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC18_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_gender_igual_a_un_id_inexistente(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        StaticData.non_existing_id.value
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC19_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_gender_vacio(
        teardown_function_remove_customer):
    random_email = Utils.get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(
        random_email,
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        StaticData.empty_name.value
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC20_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_gender_igual_a_texto(
        teardown_function_remove_customer):
    random_text = Utils.get_random_letters(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        random_text
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC21_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_gender_igual_a_simbolos(setup_data):
    random_symbols = Utils.get_random_symbols(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        random_symbols
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC22_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_store_id_igual_a_un_id_inexistente(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        StaticData.non_existing_id.value
    )
    assert_response_status(TestData.response_status_code, 404)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_404_request_does_not_match.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC23_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_store_id_vacio(
        teardown_function_remove_customer):
    random_email = Utils.get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(
        random_email,
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        StaticData.empty_name.value
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC24_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_store_id_igual_a_texto(
        teardown_function_remove_customer):
    random_text = Utils.get_random_letters(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        random_text
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC25_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_store_id_igual_a_simbolos(setup_data):
    random_symbols = Utils.get_random_symbols(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        random_symbols
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC26_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_website_id_igual_a_un_id_inexistente(
        teardown_function_remove_customer):
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        StaticData.non_existing_id.value
    )
    assert_response_status(TestData.response_status_code, 404)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_404_request_does_not_match.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC27_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_website_id_vacio(
        teardown_function_remove_customer):
    random_email = Utils.get_random_email()
    TestData.function_response_json = send_request_of_create_a_customer(
        random_email,
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        StaticData.empty_name.value
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC28_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_website_id_igual_a_texto(
        teardown_function_remove_customer):
    random_text = Utils.get_random_letters(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        random_text
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C2TC29_POST_verificar_crear_nueva_cuenta_customer_con_el_parametro_website_id_igual_a_simbolos(setup_data):
    random_symbols = Utils.get_random_symbols(5)
    TestData.function_response_json = send_request_of_create_a_customer(
        Utils.get_random_email(),
        StaticData.firstname.value,
        StaticData.lastname.value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        random_symbols
    )
    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(TestData.function_response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)

