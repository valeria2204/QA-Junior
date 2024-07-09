import pytest
import requests
from src.assertions.assertions import assert_response_status
from src.enums.static_data import StaticData
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from tests.helpers.utils import Utils
from tests.customer_group.setup import setup_module
from src.testdata import TestData
from tests.customer.setup import send_request_obtener_customer_by_id
from tests.customer_group.setup import send_request_of_update_customer_group_default, send_request_of_obtain_customer_group_by_id, send_request_of_create_a_customer_group
from src.enums.method import Method
from src.assertions.assertions import assert_equals
@pytest.mark.smoke
def test_CG03TC1_PUT_status_code_200_valido(setup_module):
    send_request_of_update_customer_group_default(TestData.module_response_json["id"])
    assert_response_status(TestData.response_status_code, 200)

@pytest.mark.smoke
def test_CG03TC2_PUT_asignar_predeterminado_a_uno_ya_predeterminado(setup_module):
    send_request_of_update_customer_group_default(1)
    assert_response_status(TestData.response_status_code, 200)

@pytest.mark.smoke
def test_CG03TC3_PUT_status_code_401_sin_autenticacion(setup_module):
    send_request_of_update_customer_group_default(TestData.module_response_json["id"], token=TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)

@pytest.mark.smoke
def test_CG03TC4_PUT_status_code_404_no_existente(setup_module):
    send_request_of_update_customer_group_default(StaticData.non_existing_id.value)
    assert_response_status(TestData.response_status_code, 404)

@pytest.mark.functional
def test_CG03TC5_PUT_status_code_400_id_invalido_texto(setup_module):
    send_request_of_update_customer_group_default(Utils.get_random_letters(5))
    assert_response_status(TestData.response_status_code, 400)

@pytest.mark.functional
def test_CG03TC6_PUT_status_code_400_id_invalido_simbolos(setup_module):
    send_request_of_update_customer_group_default(StaticData.symbols.value)
    assert_response_status(TestData.response_status_code, 400)

@pytest.mark.functional
def test_CG03TC7_PUT_status_code_400_id_vacio(setup_module):
    send_request_of_update_customer_group_default(StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 400)

@pytest.mark.functional
def test_CG03TC8_GET_en_vez_de_PUT(setup_module):
    send_request_of_update_customer_group_default(StaticData.empty_name.value, None, Method.GET.value)
    assert_response_status(TestData.response_status_code, 200)

@pytest.mark.functional
def test_CG03TC9_DELETE_en_vez_de_PUT(setup_module):
    send_request_of_update_customer_group_default(StaticData.empty_name.value, None, Method.DELETE.value)
    assert_response_status(TestData.response_status_code, 400)

@pytest.mark.functional
def test_CG03TC10_POST_en_vez_de_PUT(setup_module):
    send_request_of_update_customer_group_default(StaticData.empty_name.value, None, Method.POST.value)
    assert_response_status(TestData.response_status_code, 404)

@pytest.mark.regression
def test_CG03TC11_verificar_que_la_asignacion_de_un_customer_group_preterminado_no_afecta_obtener_customers_existentes_con_customer_group_no_predeterminados(setup_module):
    send_request_of_update_customer_group_default(TestData.module_response_json["id"])
    response_customer = send_request_obtener_customer_by_id(StaticData.customer_10.value)
    assert_equals(response_customer["id"], 10 )
