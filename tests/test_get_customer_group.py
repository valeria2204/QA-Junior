import jsonschema
import pytest

from src.singleton import Singleton


def test_schema_get_customer_group(get_body_customer_group):
    response_data = get_body_customer_group
    schema = Singleton.read_schema_json_file('get_customer_group.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')

