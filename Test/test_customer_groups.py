import pytest
import requests

# URL base para el endpoint de Magento
BASE_URL = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default/"

# Token de autenticación
AUTH_TOKEN = "psz0zk8oqeetwpgt5i0x91a1jprqfgch"

# Función para obtener los headers, incluyendo o no el token de autenticación
def get_headers(include_auth=True):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    if include_auth:
        headers['Authorization'] = f'Bearer {AUTH_TOKEN}'
    return headers

# Smoke Test - Pruebas básicas para asegurar que las funcionalidades esenciales funcionan
def test_smoke_valid_store_id():
    # Prueba con un storeId válido
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 200

def test_smoke_invalid_store_id():
    # Prueba con un storeId no válido
    store_id = 'invalid'
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 400

def test_smoke_no_auth_token():
    # Prueba sin token de autenticación
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers(include_auth=False))
    assert response.status_code == 401

# Functional Test - Pruebas funcionales para verificar que las características específicas funcionen según lo esperado
def test_functional_valid_store_id_response():
    # Verificar que el endpoint devuelve correctamente el grupo de clientes predeterminado con un storeId válido
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 200
    json_response = response.json()
    assert 'id' in json_response
    assert 'code' in json_response
    assert 'tax_class_id' in json_response

def test_functional_invalid_store_id_error():
    # Verificar que el endpoint devuelve un error 400 con un storeId no válido
    store_id = 'invalid'
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 400

def test_functional_no_auth_token_error():
    # Verificar que el endpoint devuelve un error 401 cuando el token de autorización está ausente
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers(include_auth=False))
    assert response.status_code == 401

def test_functional_valid_store_id_json_structure():
    # Verificar que la estructura del JSON devuelto es correcta para un storeId válido
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert 'id' in json_response
    assert 'code' in json_response
    assert 'tax_class_id' in json_response
    assert 'tax_class_name' in json_response

def test_functional_missing_store_id_handling():
    # Verificar que el endpoint maneja adecuadamente un storeId ausente en la solicitud
    response = requests.get(BASE_URL, headers=get_headers())
    print("Response status code:", response.status_code)
    print("Response text:", response.text)
    assert response.status_code == 200

# Regression Testing - Pruebas de regresión para asegurar que los cambios no rompan las funcionalidades existentes
def test_regression_valid_store_id_consistency():
    # Verificar que el estado HTTP 200 se mantiene para un storeId válido después de actualizaciones en el sistema
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 200

def test_regression_invalid_store_id_consistency():
    # Verificar que el estado HTTP 400 se mantiene para un storeId no válido después de actualizaciones en el sistema
    store_id = 'invalid'
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 400

def test_regression_no_auth_token_consistency():
    # Verificar que el estado HTTP 401 se mantiene cuando el Authorization token está ausente después de actualizaciones en el sistema
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers(include_auth=False))
    assert response.status_code == 401

def test_regression_valid_store_id_json_structure():
    # Verificar que no hay regresión en la estructura del JSON devuelto para un storeId válido
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert 'id' in json_response
    assert 'code' in json_response
    assert 'tax_class_id' in json_response
    assert 'tax_class_name' in json_response

def test_regression_store_id_handling_post_update():
    # Verificar que el endpoint maneja adecuadamente los storeId después de una actualización en el sistema
    store_id = 1
    response = requests.get(f"{BASE_URL}{store_id}", headers=get_headers())
    assert response.status_code == 200
