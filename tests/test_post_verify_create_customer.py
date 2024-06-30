import jsonschema
import pytest

from src.singleton import Singleton

@pytest.mark.skip(reason="Aun no se creo get_body_of_create_a_customer_with_basic_information fixture")
def test_C2TC7_POST_validar_esquema_crear_nueva_cuenta_customer_solo_con_la_informacion_valida_requerida(
        get_body_of_create_a_customer_with_basic_information):
    response_data = get_body_of_create_a_customer_with_basic_information
    schema = Singleton.read_schema_json_file('post_create_customer.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')

@pytest.mark.skip(reason="Aun no se creo get_body_of_create_a_customer_with_basic_information fixture")
def test_C2TC8_POST_validar_esquema_crear_nueva_cuenta_customer_con_todo_el_esquema_llenado(get_body_of_create_a_customer_with_full_information):
    response_data = get_body_of_create_a_customer_with_full_information
    schema = Singleton.read_schema_json_file('post_create_customer_full_information.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')
