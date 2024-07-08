import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.assertions.assertions_schema import assert_schemas
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.customer.setup import setup_function, send_request_of_update_a_customer
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C11TC1_PUT_verificar_status_code_200_cuando_se_actualiza_los_requerimientos_minimos_del_customer(setup_function):
    new_email = Utils.get_random_email()
    new_first_name = Utils.get_random_letters(5)
    new_last_name = Utils.get_random_letters(5)
    TestData.function_response_json[StaticData.email.name] = new_email
    TestData.function_response_json[StaticData.firstname.name] = new_first_name
    TestData.function_response_json[StaticData.lastname.name] = new_last_name
    send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C11TC2_PUT_validar_esquema_verificar_la_actualizacion_los_requerimientos_minimos_del_customer(setup_function):
    new_email = Utils.get_random_email()
    new_first_name = Utils.get_random_letters(5)
    new_last_name = Utils.get_random_letters(5)
    TestData.function_response_json[StaticData.email.name] = new_email
    TestData.function_response_json[StaticData.firstname.name] = new_first_name
    TestData.function_response_json[StaticData.lastname.name] = new_last_name
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_schemas(TestData.function_response_json, SchemaName.post_customer.value)
    assert_equals(response_json[StaticData.email.name], new_email)
    assert_equals(response_json[StaticData.firstname.name], new_first_name)
    assert_equals(response_json[StaticData.lastname.name], new_last_name)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C11TC3_PUT_verificar_status_code_200_cuando_se_actualiza_toda_la_informacion_de_un_customer(setup_function):
    new_email = Utils.get_random_email()
    TestData.function_response_json[StaticData.email.name] = new_email
    new_first_name = Utils.get_random_letters(5)
    TestData.function_response_json[StaticData.firstname.name] = new_first_name
    new_last_name = Utils.get_random_letters(5)
    TestData.function_response_json[StaticData.lastname.name] = new_last_name
    TestData.function_response_json[StaticData.group_id.name] = StaticData.second_group_id.value
    current_date = Utils.random_current_date()
    TestData.function_response_json[StaticData.default_billing.name] = current_date
    TestData.function_response_json[StaticData.default_shipping.name] = current_date
    past_date = Utils.random_past_date()
    TestData.function_response_json[StaticData.created_at.name] = past_date
    random_name = Utils.get_random_letters(5)
    TestData.function_response_json[StaticData.created_in.name] = random_name
    TestData.function_response_json[StaticData.dob.name] = past_date
    TestData.function_response_json[StaticData.middlename.name] = random_name
    TestData.function_response_json[StaticData.prefix.name] = random_name
    TestData.function_response_json[StaticData.suffix.name] = random_name
    TestData.function_response_json[f'{StaticData.gender=}'.split('=')[0].split('.')[1]] = StaticData.female.value

    response_json_customer = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 200)
    assert_equals(response_json_customer[StaticData.email.name], new_email)
    assert_equals(response_json_customer[StaticData.firstname.name], new_first_name)
    assert_equals(response_json_customer[StaticData.group_id.name], StaticData.second_group_id.value)
    assert_equals(response_json_customer[StaticData.default_billing.name], current_date.split('-')[0])
    assert_equals(response_json_customer[StaticData.default_shipping.name], current_date.split('-')[0])
    assert_equals(response_json_customer[StaticData.created_at.name], past_date)
    assert_equals(response_json_customer[StaticData.created_in.name], StaticData.created_in.value)
    assert_equals(response_json_customer[StaticData.dob.name], past_date.split(' ')[0])
    assert_equals(response_json_customer[StaticData.middlename.name], random_name)
    assert_equals(response_json_customer[StaticData.prefix.name], random_name)
    assert_equals(response_json_customer[StaticData.suffix.name], random_name)
    assert_equals(response_json_customer[f'{StaticData.gender=}'.split('=')[0].split('.')[1]], StaticData.female.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC4_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valores_vacios_para_todos_los_req_vacios(setup_function):
    TestData.function_response_json[StaticData.email.name] = StaticData.empty_name.value
    TestData.function_response_json[StaticData.firstname.name] = StaticData.empty_name.value
    TestData.function_response_json[StaticData.lastname.name] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], 'The customer email is missing. Enter and try again.')


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC5_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valor_vacio_para_email(setup_function):
    TestData.function_response_json[StaticData.email.name] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], 'The customer email is missing. Enter and try again.')


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC6_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valor_solo_texto_para_email(setup_function):
    TestData.function_response_json[StaticData.email.name] = Utils.get_random_letters(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], '"Email" is not a valid email address.')


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC7_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valor_solo_numerico_para_email(setup_function):
    TestData.function_response_json[StaticData.email.name] = Utils.get_random_numerics(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], '"Email" is not a valid email address.')


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC8_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valor_solo_simbolos_para_email(setup_function):
    TestData.function_response_json[StaticData.email.name] = Utils.get_random_symbols(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], '"Email" is not a valid email address.')


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC9_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valor_vacio_para_first_name(setup_function):
    TestData.function_response_json[StaticData.firstname.name] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], '"First Name" is a required value.')

@pytest.mark.functional
@pytest.mark.regression
def test_C11TC10_PUT_verificar_status_code_400_cuando_se_actualiza_un_customer_con_valor_vacio_para_last_name(setup_function):
    TestData.function_response_json[StaticData.lastname.name] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], '"Last Name" is a required value.')


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC11_PUT_verificar_la_actualizacion_de_customer_con_el_group_id_vacio(setup_function):
    TestData.function_response_json[StaticData.group_id.name] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], "Error occurred during \"group_id\" processing. The \"\" value's type is invalid. The \"int\" type was expected. Verify and try again.")


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC12_PUT_verificar_la_actualizacion_de_customer_con_el_group_id_igual_a_texto(setup_function):
    random_text = Utils.get_random_letters(5)
    TestData.function_response_json[StaticData.group_id.name] = random_text
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], f"Error occurred during \"group_id\" processing. The \"{random_text}\" value's type is invalid. The \"int\" type was expected. Verify and try again.")


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC13_PUT_verificar_la_actualizacion_de_customer_con_el_group_id_igual_a_simbolos(setup_function):
    random_symbols = Utils.get_random_symbols(5)
    TestData.function_response_json[StaticData.group_id.name] = random_symbols
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)
    assert_equals(response_json["message"], f"Error occurred during \"group_id\" processing. The \"{random_symbols}\" value's type is invalid. The \"int\" type was expected. Verify and try again.")


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC14_PUT_verificar_la_actualizacion_de_customer_con_el_group_id_igual_a_un_id_inexistente(setup_function):
    TestData.function_response_json[StaticData.group_id.name] = Utils.get_random_numerics(10)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(response_json, SchemaName.post_customer.value)
    assert_equals(response_json["group_id"], StaticData.group_id.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC15_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_created_in_vacio(setup_function):
    TestData.function_response_json[StaticData.created_in.name] = StaticData.empty_name.value
    send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC16_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_created_in_igual_a_texto(setup_function):
    TestData.function_response_json[StaticData.created_in.name] = Utils.get_random_letters(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(response_json, SchemaName.post_customer.value)
    assert_equals(response_json[StaticData.created_in.name], StaticData.created_in.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC17_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_created_in_igual_a_simbolos(setup_function):
    TestData.function_response_json[StaticData.created_in.name] = Utils.get_random_symbols(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(response_json, SchemaName.post_customer.value)
    assert_equals(response_json[StaticData.created_in.name], StaticData.created_in.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC18_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_gender_igual_a_un_id_inexistente(setup_function):
    TestData.function_response_json[f'{StaticData.gender=}'.split('=')[0].split('.')[1]] = Utils.get_random_symbols(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC19_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_gender_vacio(setup_function):
    TestData.function_response_json[f'{StaticData.gender=}'.split('=')[0].split('.')[1]] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC20_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_gender_igual_a_texto(setup_function):
    TestData.function_response_json[f'{StaticData.gender=}'.split('=')[0].split('.')[1]] = Utils.get_random_letters(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC21_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_gender_igual_a_simbolos(setup_function):
    TestData.function_response_json[f'{StaticData.gender=}'.split('=')[0].split('.')[1]] = Utils.get_random_symbols(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC22_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_store_id_igual_a_un_id_inexistente(setup_function):
    TestData.function_response_json[f'{StaticData.store_id=}'.split('=')[0].split('.')[1]] = StaticData.non_existing_id.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 404)
    assert_schemas(response_json, SchemaName.response_status_code_404_no_such_entity.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC23_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_store_id_vacio(setup_function):
    TestData.function_response_json[f'{StaticData.store_id=}'.split('=')[0].split('.')[1]] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC24_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_store_id_igual_a_texto(setup_function):
    TestData.function_response_json[f'{StaticData.store_id=}'.split('=')[0].split('.')[1]] = Utils.get_random_letters(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC25_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_store_id_igual_a_simbolos(setup_function):
    TestData.function_response_json[f'{StaticData.store_id=}'.split('=')[0].split('.')[1]] = Utils.get_random_symbols(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC26_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_website_id_igual_a_un_id_inexistente(setup_function):
    TestData.function_response_json[f'{StaticData.website_id=}'.split('=')[0].split('.')[1]] = StaticData.non_existing_id.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 404)
    assert_schemas(response_json, SchemaName.response_status_code_404_no_such_entity.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC27_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_website_id_vacio(setup_function):
    TestData.function_response_json[f'{StaticData.website_id=}'.split('=')[0].split('.')[1]] = StaticData.empty_name.value
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC28_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_website_id_igual_a_texto(setup_function):
    TestData.function_response_json[f'{StaticData.website_id=}'.split('=')[0].split('.')[1]] = Utils.get_random_letters(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)


@pytest.mark.functional
@pytest.mark.regression
def test_C11TC29_PUT_verificar_la_actualizacion_de_customer_con_el_parametro_website_id_igual_a_simbolos(setup_function):
    TestData.function_response_json[f'{StaticData.website_id=}'.split('=')[0].split('.')[1]] = Utils.get_random_symbols(5)
    response_json = send_request_of_update_a_customer(TestData.function_response_json[StaticData.id.name], TestData.function_response_json)

    assert_response_status(TestData.response_status_code, 400)
    assert_schemas(response_json, SchemaName.response_status_code_400_type_value_is_invalid.value)

