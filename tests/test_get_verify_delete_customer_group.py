import pytest
import requests

from src.singleton import Singleton


@pytest.mark.smoke
def test_CG9TC1_GET_verificar_si_un_customer_group_no_asignado_un_customer_puede_ser_eliminado(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/0/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data is True


@pytest.mark.smoke
def test_CG9TC2_GET_verificar_si_un_customer_group_puede_ser_eliminado_por_un_id_no_existente(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1000/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 404
    assert response_data["message"] == 'No such entity with %fieldName = %fieldValue'
    assert response_data["parameters"]["fieldName"] == "groupId"
    assert response_data["parameters"]["fieldValue"] == 1000


@pytest.mark.functional
def test_CG9TC3_GET_verificar_si_un_customer_group_puede_ser_eliminado_con_un_id_vacio(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups//permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 400
    assert response_data["message"] == "The \"\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.functional
def test_CG9TC4_GET_verificar_si_un_customer_group_asignado_a_un_customer_puede_ser_eliminado(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/2/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 200
    assert str(response_data) is "False"


@pytest.mark.functional
def test_CG9TC5_GET_verificar_la_solicitud_de_permisos_de_eliminacion_de_customer_group_con_parametro_alfabetico(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/s/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 400
    assert response_data["message"] == "The \"s\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.functional
def test_CG9TC6_GET_verificar_la_solicitud_de_permisos_de_eliminacion_de_customer_group_con_parametro_de_caracter_especial(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/$/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 400
    assert response_data["message"] == "The \"$\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.functional
def test_CG9TC7_GET_verificar_la_solicitud_de_permisos_de_eliminacion_de_customer_group_con_bearer_token_no_valido():
    token = Singleton.get_token_no_valid()
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/0/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 401
    assert response_data["message"] == "The consumer isn't authorized to access %resources."
    assert response_data["parameters"]["resources"] == "Magento_Customer::group"
