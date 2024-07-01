import json

import pytest
import requests

from src.assertions.asserions_schema import assert_schemas
from src.singleton import Singleton
from tests.conftest import send_request_of_check_if_non_existent_customer_group_can_be_deleted
from tests.conftest import send_request_of_check_if_customer_group_can_be_deleted_with_empty_id

@pytest.mark.smoke
@pytest.mark.functional
def test_CG9TC1_GET_verificar_si_un_customer_group_no_asignado_a_un_customer_puede_ser_eliminado(get_token_login):
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


@pytest.mark.functional
def test_CG9TC2_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_no_existente(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1000/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 404
    assert response_data["parameters"]["fieldValue"] == 1000


@pytest.mark.functional
def test_CG9TC3_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_vacio(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups//permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 400


@pytest.mark.smoke
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


@pytest.mark.regression
def test_CG9TC5_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_tipo_texto(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/s/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 400


@pytest.mark.regression
def test_CG9TC6_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_caracter_especial(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/$/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 400


@pytest.mark.functional
def test_CG9TC7_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_token_no_tiene_permisos():
    token = Singleton.get_token_no_valid()
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/0/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 401


@pytest.mark.regression
def test_CG9TC12_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 404


@pytest.mark.regression
def test_CG9TC13_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    assert response.status_code == 404


@pytest.mark.regression
def test_CG9TC14_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    assert response.status_code == 404


@pytest.mark.smoke
def test_CG9TC8_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_no_existente(
    send_request_of_check_if_non_existent_customer_group_can_be_deleted):
    assert_schemas(Singleton.response_404_json, 'response_status_code_404_no_such_entity.json')
    assert Singleton.response_404_json["message"] == 'No such entity with %fieldName = %fieldValue'
    assert Singleton.response_404_json["parameters"]["fieldName"] == "groupId"


@pytest.mark.regression
def test_CG9TC9_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_vacio(send_request_of_check_if_customer_group_can_be_deleted_with_empty_id):
    assert_schemas(Singleton.response_400_json, 'response_status_code_400_type_value_is_invalid.json')
    assert Singleton.response_400_status_code == 400
    assert Singleton.response_400_json["message"] == "The \"\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.regression
def test_CG9TC10_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_tipo_texto(send_request_of_check_if_customer_group_can_be_deleted_with_id_of_string_type):
    assert_schemas(Singleton.response_400_json, 'response_status_code_400_type_value_is_invalid.json')
    assert Singleton.response_400_status_code == 400
    assert Singleton.response_400_json["message"] == "The \"texto\" value's type is invalid. The \"int\" type was expected. Verify and try again."



@pytest.mark.regression
def test_CG9TC11_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_id_es_de_caracter_especial(send_request_of_check_if_customer_group_can_be_deleted_with_id_of_special_character_type):
    assert_schemas(Singleton.response_400_json, 'response_status_code_400_type_value_is_invalid.json')
    assert Singleton.response_400_status_code == 400
    assert Singleton.response_400_json["message"] == "The \"$$$$$\" value's type is invalid. The \"int\" type was expected. Verify and try again."


@pytest.mark.functional
def test_CG9TC15_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_el_token_no_tiene_permisos(send_request_of_check_if_customer_group_can_be_deleted_with_token_no_valid):
    assert_schemas(Singleton.response_401_json, 'response_status_code_400_type_value_is_invalid.json')
    assert Singleton.response_401_status_code == 401
    assert Singleton.response_401_json["message"] == "The consumer isn't authorized to access %resources."
    assert Singleton.response_401_json["parameters"]["resources"] == "Magento_Customer::group"


@pytest.mark.regression
def test_CG9TC12_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 404


@pytest.mark.regression
def test_CG9TC13_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    assert response.status_code == 404


@pytest.mark.regression
def test_CG9TC14_GET_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    assert response.status_code == 404


@pytest.mark.regression
def test_CG9TC16_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_post(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    assert_schemas(response_json, 'response_status_code_404_request_does_not_match.json')
    assert response_json["message"] == "Request does not match any route."


@pytest.mark.regression
def test_CG9TC17_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_put(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    assert_schemas(response_json, 'response_status_code_404_request_does_not_match.json')
    assert response_json["message"] == "Request does not match any route."


@pytest.mark.regression
def test_CG9TC18_GET_verificar_esquema_verificar_si_un_customer_group_puede_ser_eliminado_cuando_se_usa_el_metodo_delete(get_token_login):
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/1/permissions"

    payload = {}
    headers = {
        'Authorization': f'Bearer {get_token_login}',
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    assert_schemas(response_json, 'response_status_code_404_request_does_not_match.json')
    assert response_json["message"] == "Request does not match any route."

