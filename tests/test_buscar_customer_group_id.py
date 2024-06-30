import pytest
import requests

from src.singleton import Singleton


@pytest.mark.functional
def test_CG_05_TC4_POST_verificar_codigo_de_error_en_endpoint(get_token_login):
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
def test_CG_05_TC5_PUT_Verificar_codigo_de_error_en_endpoint(get_token_login):
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
def test_CG_05_TC6_DELETE__Verificar_codigo_de_error_en_endpoint(get_token_login):
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

@pytest.mark.regression
def test_CG_05_TC8_POST_verificar_codigo_de_error_en_endpoint(get_token_login):
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


@pytest.mark.regression
def test_CG_05_TC9_PUT_Verificar_codigo_de_error_en_endpoint(get_token_login):
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


@pytest.mark.regression
def test_CG_05_TC10_DELETE__Verificar_codigo_de_error_en_endpoint(get_token_login):
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
