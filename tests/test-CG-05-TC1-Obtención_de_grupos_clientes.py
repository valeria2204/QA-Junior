import jsonschema
import pytest

from src.singleton import Singleton


def test_schema_customer_group_por_id(get_body_customer_group_por_id):
    response_data = get_body_customer_group_por_id
    schema = Singleton.read_schema_json_file('get_customer_group_por_id.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')

