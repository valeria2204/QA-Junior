import pytest
import requests

from src.assertions.esquema_assertion import assert_validate_schema
from src.singleton import Singleton


def test_CG2TC1_GET_verificar_la_obtencion_exitosa_de_CustomerGroup_por_defecto(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200


def test_CG2TC2_GET_verificar_esquema_obtencion_exitosa_de_CustomerGroup_por_defecto(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    esquema = Singleton.read_schema_json_file("get_customer_group.json")
    assert assert_validate_schema(response.json(), esquema)


def test_CG2TC3_GET_validar_respuesta_401_al_enviar_un_token_invalido(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": "Bearer Token"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 401


def test_CG2TC4_GET_validar_respuesta_401_al_enviar_la_solicitud_sin_el_header_Authorization(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.text
    assert response.status_code == 401


def test_CG2TC5_GET_verificar_que_la_respuesta_tenga_un_id_numero_entero_positivo(get_token_login):
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


def test_CG2TC6_GET_verificar_que_la_respuesta_tenga_un_class_id_numero_entero_positivo(get_token_login):
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


def test_CG2TC7_GET_verificar_que_la_respuesta_tenga_un_code_cadena_no_vacia(get_token_login):
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


def test_CG2TC8_GET_verificar_que_la_respuesta_tenga_un_tax_class_name_cadena_no_vacia(get_token_login):
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


def test_CG2TC9_GET_verificar_que_el_resultado_no_se_ve_afectado_cuando_se_envia_un_parametro_de_consulta(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/default?code=LoremIpsum"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 1
