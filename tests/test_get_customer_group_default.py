import pytest
import requests
import jsonschema


esquema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "code": {
      "type": "string"
    },
    "tax_class_id": {
      "type": "integer"
    },
    "tax_class_name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "code",
    "tax_class_id",
    "tax_class_name"
  ]
}

def test_validar_request_retorna_codigo_200(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200

def test_validar_esquema(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    try:
        jsonschema.validate(instance=response.json(), schema=esquema)
    except jsonschema.exceptions.ValidationError as err:
        assert False


def test_verificar_codigo_respuesta_401_token_invalido(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": "Bearer Token"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 401

def test_verificar_respuesta_sin_enviar_token(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.text
    assert response.status_code == 401

def test_validar_el_campo_id(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert isinstance(res["id"], int)
    assert res["id"] >= 0

def test_validar_el_campo_tax_class_id(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert isinstance(res["tax_class_id"], int)
    assert res["tax_class_id"] >= 0

def test_validar_que_el_campo_code_sea_string(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert isinstance(res["code"], str)
    assert len(res["code"]) >= 0

def test_validar_que_el_campo_tax_class_name_sea_string(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert isinstance(res["tax_class_name"], str)
    assert len(res["tax_class_name"]) >= 0

def test_validar_que_el_un_parametrop_de_consulta_no_afecta_resultado(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default?code=LoremIpsum"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    res = response.json()
    assert res["id"] == 1
