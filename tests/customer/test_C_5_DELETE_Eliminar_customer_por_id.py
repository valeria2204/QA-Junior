import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.customer.setup import setup_module, send_request_of_create_a_customer, setup_function, \
    send_request_of_remove_customer

from tests.conftest import setup_data
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC1_DELETE_verificar_status_code_200_al_eliminar_un_customer_nuevo(setup_function):
    email = Utils.get_random_email()
    firstname = StaticData.firstname.value
    lastname = StaticData.lastname.value
    send_request_of_create_a_customer(email, firstname, lastname)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC2_DELETE_verificar_status_code_400_al_eliminar_un_customer_con_customer_id_invalido_de_tipo_simbolo(setup_function):
    customer_id = Utils.get_random_symbols(1)
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC3_DELETE_verificar_status_code_404_al_eliminar_un_customer_con_customer_id_invalido_de_tipo_letra(setup_function):
    customer_id = Utils.get_random_letters(2)
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C5TC4_DELETE_verificar_status_code_404_al_eliminar_un_customer_con_customer_id_vacio(setup_function):
    customer_id = Utils.get_random_letters(2)
    send_request_of_remove_customer(customer_id)
    assert_response_status(TestData.response_status_code, 400)