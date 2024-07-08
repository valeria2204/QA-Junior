import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.assertions.assertions_schema import assert_schemas
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.testdata import TestData
from tests.customer.setup import setup_function, send_request_of_remove_customer, setup_function_full_customer, \
    send_request_of_create_a_customer
from tests.helpers.utils import Utils
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C14TC1_DELETE_verificar_status_code_200_al_eliminar_un_customer_nuevo(setup_data):
    email = Utils.get_random_email()
    firstname = StaticData.firstname.value
    lastname = StaticData.lastname.value
    TestData.function_response_json = send_request_of_create_a_customer(email, firstname, lastname)
    assert_response_status(TestData.response_status_code, 200)