import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.customer.setup import setup_module, send_request_of_create_a_customer, setup_function, \
    send_request_of_remove_customer

from tests.conftest import setup_data

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_existing_customer(setup_function):
    send_request_of_create_a_customer("tati8@gmail.com", "Tati", "Mayo")
    assert_response_status(TestData.response_status_code, 200)


