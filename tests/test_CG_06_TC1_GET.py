import pytest
import requests

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

