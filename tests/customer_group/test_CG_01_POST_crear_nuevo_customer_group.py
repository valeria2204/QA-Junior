import json

import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer_group.setup import send_request_of_obtain_default_customer_group_by, \
    send_request_of_create_a_customer_group


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC1_POST_Crear_nuevo_Customer_Group_con_token_de_autentication_valida_y_con_body_vacio(setup_data):
    payload = json.dumps({})
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 400)

