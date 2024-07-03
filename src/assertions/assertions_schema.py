import jsonschema
import pytest

from tests.helpers.utils import Utils


def assert_schemas(response_data, json_name):
    schema = Utils().read_schema_json_file(json_name)
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')
