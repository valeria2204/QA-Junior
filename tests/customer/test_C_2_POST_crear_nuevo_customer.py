import pytest

from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import send_request_of_create_a_customer
from tests.conftest import setup_data
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C2TC7_POST_validar_esquema_crear_nueva_cuenta_customer_solo_con_la_informacion_valida_requerida(setup_data):
    random_value = Utils().get_random_alphanumeric(4)
    send_request_of_create_a_customer(f"{random_value}@gmail.com", random_value, random_value)
    assert_schemas(TestData.response_json, 'post_create_customer.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C2TC8_POST_validar_esquema_crear_nueva_cuenta_customer_con_todo_el_esquema_llenado(setup_data):
    random_value = Utils().get_random_alphanumeric(4)
    send_request_of_create_a_customer(f"{random_value}@gmail.com", random_value, random_value)
    assert_schemas(TestData.response_json, 'post_create_customer_full_information.json')
