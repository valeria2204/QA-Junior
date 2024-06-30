import pytest
import requests
import jsonschema

from src.assertions.schema_assertion import assert_validate_schema
from src.json_handler import read_json
from src.singleton import Singleton


ENDPOINT = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"
ESQUEMA = "get_customer_groups_default.json"

def test_validar_request_retorna_codigo_200(get_token_login):
    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 200

def test_validar_esquema(get_token_login):
    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 200
    assert assert_validate_schema(response.json(), read_json(ESQUEMA))


def test_verificar_codigo_respuesta_401_token_invalido(get_token_login):
    payload = {}
    headers = {
        "Authorization": "Bearer Token"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 401

def test_verificar_respuesta_sin_enviar_token(get_token_login):
    payload = {}
    headers = {}

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)
    assert response.text
    assert response.status_code == 401

def test_validar_el_campo_id(get_token_login):
    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert assert_validate_schema(res, read_json(ESQUEMA))
    assert isinstance(res["id"], int)
    assert res["id"] >= 0

def test_validar_el_campo_tax_class_id(get_token_login):
    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert assert_validate_schema(res, read_json(ESQUEMA))
    assert isinstance(res["tax_class_id"], int)
    assert res["tax_class_id"] >= 0

def test_validar_que_el_campo_code_sea_string(get_token_login):
    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert assert_validate_schema(res, read_json(ESQUEMA))
    assert isinstance(res["code"], str)
    assert len(res["code"]) >= 0

def test_validar_que_el_campo_tax_class_name_sea_string(get_token_login):
    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", ENDPOINT, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert assert_validate_schema(res, read_json(ESQUEMA))
    assert isinstance(res["tax_class_name"], str)
    assert len(res["tax_class_name"]) >= 0

def test_validar_que_el_un_parametrop_de_consulta_no_afecta_resultado(get_token_login):
    url = f"{ENDPOINT}?code=LoremIpsum"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert assert_validate_schema(res, read_json(ESQUEMA))
    assert res["id"] == 1
