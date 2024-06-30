import jsonschema
import pytest

from src.singleton import Singleton


def test_schema_verificar_obtencion_exitosa_de_los_customer_groups(get_body_obtain_first_10_customer_groups):
    response_data = get_body_obtain_first_10_customer_groups
    schema = Singleton.read_schema_json_file('get_obtain_first_10_customer_groups.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')

