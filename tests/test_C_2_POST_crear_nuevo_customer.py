import pytest

from src.assertions.assertions_schema import assert_schemas


@pytest.mark.smoke
def test_C2TC7_POST_validar_esquema_crear_nueva_cuenta_customer_solo_con_la_informacion_valida_requerida(
        get_body_of_create_a_customer_with_basic_information):
    response_data = get_body_of_create_a_customer_with_basic_information
    assert_schemas(response_data, 'post_create_customer.json')


@pytest.mark.smoke
def test_C2TC8_POST_validar_esquema_crear_nueva_cuenta_customer_con_todo_el_esquema_llenado(get_body_of_create_a_customer_with_full_information):
    response_data = get_body_of_create_a_customer_with_full_information
    assert_schemas(response_data, 'post_create_customer_full_information.json')
