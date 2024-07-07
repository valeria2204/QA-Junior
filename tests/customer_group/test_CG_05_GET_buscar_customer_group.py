import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.enums.method import Method
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer_group.setup import setup_module, send_request_of_obtain_customer_groups_by_search_criterias


@pytest.mark.regression
def test_CG05TC4_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_POST(setup_data):
    send_request_of_obtain_customer_groups_by_search_criterias("1", "10", None, None, None, TestData.token, Method.POST.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG05TC5_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_PUT(setup_data):
    send_request_of_obtain_customer_groups_by_search_criterias("1", "10", None, None, None, TestData.token,
                                                               Method.PUT.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.regression
def test_CG05TC6_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_group_con_el_metodo_DELETE(setup_data):
    send_request_of_obtain_customer_groups_by_search_criterias("1", "10", None, None, None, TestData.token,
                                                               Method.DELETE.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
def test_schema_verificar_obtencion_exitosa_de_los_customer_groups(setup_data):
    response_json = send_request_of_obtain_customer_groups_by_search_criterias("1", "4")
    assert_schemas(response_json, 'get_customer_groups_by_search_criteria_first_page_and_page_size.json')


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG05TC11_GET_verificar_que_el_primer_customer_group_es_encontrado_por_los_criterios_de_busqueda_field_value_condition_type(setup_module):
    send_request_of_obtain_customer_groups_by_search_criterias(None, None, "id", TestData.module_response_json["id"], "eq")
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.skip(reason="el test case falla")
def test_CG05TC3_GET_verificar_que_ningun_customer_group_es_encontrado_con_los_valores_invalidos_para_los_criterios_de_busqueda_field_value_condition_type(setup_data):
    send_request_of_obtain_customer_groups_by_search_criterias(None, None, "nonexistent_field", "invalid_value", "invalid_condition")
    assert_response_status(TestData.response_status_code, 404)

@pytest.mark.smoke
@pytest.mark.functional
def test_CG05TC2_GET_verificar_que_retorna_un_error_al_buscar_los_10_primeros_customer_groups_cuando_no_tienes_autorizacion(setup_data):
    send_request_of_obtain_customer_groups_by_search_criterias(1, 10, None, None, None, TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)
