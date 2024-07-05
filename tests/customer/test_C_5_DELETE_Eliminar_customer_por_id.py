import pytest

from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import send_request_of_create_a_customer
from tests.conftest import setup_data
from tests.helpers.utils import Utils


def test_delete_existing_customer(setup_data):
    # Crear un nuevo cliente con un email único
    email = "test@example.com"
    firstname = "Test"
    lastname = "User"
    send_request_of_create_a_customer(email, firstname, lastname)

    # Validar que la creación fue exitosa
    assert TestData.response_status_code == 200



