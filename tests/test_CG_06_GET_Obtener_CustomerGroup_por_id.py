import pytest
import requests

from src.assertions.asserions_schema import assert_schemas
from src.singleton import Singleton


@pytest.mark.smoke
def test_CG6TC1_GET_verificar_obtencion_exitosa_de_customer_group_por_id(get_token_login):
    group_id = 1

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()
    assert response.status_code == 200

    
@pytest.mark.functional
def test_CG6TC2_GET_validar_esquema_obtencion_exitosa_de_customer_group_por_id(get_body_of_obtain_customer_group_by_id):
    response_data = get_body_of_obtain_customer_group_by_id
    assert_schemas(response_data, 'get_customer_group.json')

    
@pytest.mark.smoke
def test_CG6TC3_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_alfabetico(get_token_login):

    group_id = "ASD"

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400

    
@pytest.mark.functional
def test_CG6TC4_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_de_caracter_especial(get_token_login):
    group_id = "@"

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400

    
@pytest.mark.functional
def test_CG6TC5_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_vacio(get_token_login):
    group_id = ""

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 404

    
@pytest.mark.functional
def test_CG6TC6_GET_verificar_respuesta_de_error_al_solicitar_un_customer_group_con_id_no_existente(get_token_login):
    group_id = 52542542542

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 404

    
def test_CG6TC7_GET_validar_error_de_no_autorizado_al_acceder_sin_token_de_autorizacion():
    group_id = 1
    token = Singleton.get_token_no_valid()
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 401
