import jsonschema
import pytest

from src.singleton import Singleton


def test_schema_create_customer(get_body_create_customer):
    response_data = get_body_create_customer
    schema = Singleton.read_schema_json_file('post_create_customer.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')

