import pytest
import requests
from jsonschema import validate, ValidationError

# URL base de la API
base_url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups"
# Token de acceso
access_token = "psz0zk8oqeetwpgt5i0x91a1jprqfgch"

# Esquema de la respuesta esperada
response_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "code": {"type": "string"},
        "tax_class_id": {"type": "number"},
        "tax_class_name": {"type": "string"},
        "extension_attributes": {
            "type": "object",
            "properties": {
                "exclude_website_ids": {
                    "type": "array",
                    "items": {"type": "number"}
                }
            },
            "additionalProperties": False
        }
    },
    "required": ["id", "code", "tax_class_id", "tax_class_name"],
    "additionalProperties": False
}

# Caso de prueba: Verificar obtención exitosa de un grupo de clientes por ID
def test_get_customer_group_success():
    group_id = 1  # ID válido de un grupo de clientes existente
    url = f"{base_url}/{group_id}"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()

    # Verificar código de estado de la respuesta
    assert response.status_code == 200

    # Validar el esquema de la respuesta
    try:
        validate(instance=response_data, schema=response_schema)
    except ValidationError as e:
        pytest.fail(f"Respuesta no cumple con el esquema: {e.message}")

    # Verificar que las claves esperadas están en la respuesta
    assert "id" in response_data
    assert "code" in response_data
    assert "tax_class_id" in response_data
    assert "tax_class_name" in response_data

    if "extension_attributes" in response_data:
        assert response_data["extension_attributes"] is not None
