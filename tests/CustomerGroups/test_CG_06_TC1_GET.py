import pytest
import requests
import jsonschema
from src.singleton import Singleton

# URL base de la API
base_url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups"
# Token de acceso
access_token = "psz0zk8oqeetwpgt5i0x91a1jprqfgch"

# Caso de prueba 1: Verificar obtención exitosa de un grupo de clientes por ID
def test_get_customer_group_success():
    group_id = 1  # ID válido de un grupo de clientes existente
    url = f"{base_url}/{group_id}"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    response_data = response.json()

    assert response.status_code == 200
    assert "id" in response_data
    assert "code" in response_data
    assert "tax_class_id" in response_data
    assert "tax_class_name" in response_data

    if "extension_attributes" in response_data:
        assert response_data["extension_attributes"] is not None

#Validando el esquema del get
def test_schema_get_customer_group(get_body_customer_group):
    response_data = get_body_customer_group
    schema = Singleton.read_schema_json_file('get_customer_group.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')