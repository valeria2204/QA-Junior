import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.customer.setup import setup_module, send_request_of_create_a_customer
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_Verificar_status_code_200_cuando_se_crea_nueva_cuenta_customer(setup_module):
    assert_response_status(TestData.response_status_code, 200)



@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_validar_esquema_creacion_de_nueva_cuenta_customer(setup_module):
    assert_schemas(TestData.module_response_json, 'post_create_customer.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_Verificar_status_code_401_cuando_se_crea_nueva_cuenta_customer(setup_data):
    send_request_of_create_a_customer("", "", "")
    assert_response_status(TestData.response_status_code, 400)
