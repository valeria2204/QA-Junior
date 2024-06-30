import pytest
import requests

from src.assertions.esquema_assertion import assert_validate_schema
from src.singleton import Singleton

RUTA_ESQUEMA = "get_customer_group_default.json"

def test_validar_request_retorna_codigo_200(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

def test_validar_esquema(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    esquema = Singleton.read_schema_json_file(RUTA_ESQUEMA)
    assert assert_validate_schema(response.json(), esquema)

def test_verificar_codigo_respuesta_401_token_invalido(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": "Bearer Token"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 401

def test_verificar_respuesta_sin_enviar_token(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.text
    assert response.status_code == 401

def test_validar_el_campo_id(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data["id"], int)
    assert response_data["id"] >= 0

def test_validar_el_campo_tax_class_id(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data["tax_class_id"], int)
    assert response_data["tax_class_id"] >= 0

def test_validar_que_el_campo_code_sea_string(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data["code"], str)
    assert len(response_data["code"]) >= 0

def test_validar_que_el_campo_tax_class_name_sea_string(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data["tax_class_name"], str)
    assert len(response_data["tax_class_name"]) >= 0

def test_validar_que_el_un_parametrop_de_consulta_no_afecta_resultado(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default?code=LoremIpsum"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 1
