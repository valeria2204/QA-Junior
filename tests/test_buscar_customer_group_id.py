import pytest
import requests

from src.singleton import Singleton


@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC4_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_POST(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    payload = {}

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()

    assert response.status_code == 404, "NO FOUND 404"


@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC5_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_PUT(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    payload = {}

    response = requests.put(url, headers=headers, json=payload)
    response_data = response.json()

    assert response.status_code == 400, "NO FOUND 400"


@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC6_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_DELETE(get_token_login):
    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/search"

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    payload = {}

    response = requests.delete(url, headers=headers, json=payload)
    response_data = response.json()

    assert response.status_code == 400, "NO FOUND 400"
