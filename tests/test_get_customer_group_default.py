import pytest
import requests


def test_validar_request_retorna_codigo_200(get_token_login):
    url = "https://magento2-demo.magebit.com/rest/default/V1/customerGroups/default"

    payload = {}
    headers = {
        "Authorization": f"Bearer {get_token_login}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200
