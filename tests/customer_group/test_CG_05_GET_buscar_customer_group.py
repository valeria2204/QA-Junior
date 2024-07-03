import pytest
import requests

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from src.testdata import TestData
from tests.conftest import send_request_of_obtain_customer_groups_by_search_criteria_first_page_and_page_size
from tests.conftest import setup_data



@pytest.mark.regression
def test_CG05TC4_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_POST(setup_data):
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}"

    payload = {}
    headers = header_content_type_authorization(TestData.token)
    response = requests.post(url, headers=headers, json=payload)

    assert_response_status(response.status_code, 404)


@pytest.mark.regression
def test_CG05TC5_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_PUT(setup_data):
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}"

    payload = {}
    headers = header_content_type_authorization(TestData.token)
    response = requests.put(url, headers=headers, json=payload)

    assert_response_status(response.status_code, 400)


@pytest.mark.regression
def test_CG05TC6_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_DELETE(setup_data):
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}"

    payload = {}
    headers = header_content_type_authorization(TestData.token)
    response = requests.delete(url, headers=headers, json=payload)

    assert_response_status(response.status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
def test_schema_verificar_obtencion_exitosa_de_los_customer_groups(setup_data):
    send_request_of_obtain_customer_groups_by_search_criteria_first_page_and_page_size("1", "4")
    assert_schemas(TestData.response_json, 'get_customer_groups_by_search_criteria_first_page_and_page_size.json')



@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC11_GET_verificar_que_el_primer_customer_group_es_encontrado_por_los_criterios_de_busqueda_field_value_condition_type(setup_data):
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}"

    params = {
        'searchCriteria[filterGroups][0][filters][0][field]': 'id',
        'searchCriteria[filterGroups][0][filters][0][value]': '1',
        'searchCriteria[filterGroups][0][filters][0][condition_type]': 'eq'
    }
    headers = header_authorization(TestData.token)
    response = requests.get(url, headers=headers, params=params)

    assert_response_status(response.status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC3_GET_verificar_que_ningun_customer_group_es_encontrado_con_los_valores_invalidos_para_los_criterios_de_busqueda_field_value_condition_type(setup_data):
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}"

    params = {
        'searchCriteria[filterGroups][0][filters][0][field]': 'nonexistent_field',
        'searchCriteria[filterGroups][0][filters][0][value]': 'invalid_value',
        'searchCriteria[filterGroups][0][filters][0][condition_type]': 'invalid_condition'
    }
    headers = header_authorization(TestData.token)
    response = requests.get(url, headers=headers, params=params)

    assert_response_status(response.status_code, 404)

@pytest.mark.smoke
@pytest.mark.functional
def test_CG05TC2_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_groups_cuando_no_tienes_autorizacion(setup_data):
    url = f"{TestData.base_url}{URIComplement.GET_SEARCH_CUSTOMER_GROUP.value}?searchCriteria[currentPage]=1&searchCriteria[pageSize]=10"

    payload = {}
    headers = header_authorization(TestData.token_no_valid)
    response = requests.request("GET", url, headers=headers, data=payload)

    assert_response_status(response.status_code, 401)
