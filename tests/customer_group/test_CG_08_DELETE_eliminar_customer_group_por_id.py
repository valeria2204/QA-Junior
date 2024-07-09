import pytest
import requests

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer_group.setup import setup_function_customer_group
from tests.customer_group.setup import send_request_of_remove_customer_group
from src.enums.uri import URIComplement
from src.headers.headers import header_authorization
from src.enums.static_data import StaticData
from src.enums.method import Method
from tests.helpers.utils import Utils


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC1_DELETE_verificar_la_eliminacion_de_un_customer_group_con_id_valido(setup_function_customer_group):
    send_request_of_remove_customer_group(TestData.function_response_json_customer_group["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC2_DELETE_verificar_la_eliminacion_de_un_customer_group_con_id_de_un_grupo_predeterminado(setup_data):
    send_request_of_remove_customer_group(StaticData.group_id.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC3_DELETE_verificar_la_eliminacion_de_un_customer_group_sin_token_de_autenticacion_con_id_valido(
        setup_function_customer_group):
    send_request_of_remove_customer_group(StaticData.group_id.value, StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
def test_CG8TC4_DELETE_verificar_la_eliminacion_de_un_customer_group_que_no_existe(setup_function_customer_group):
    send_request_of_remove_customer_group(StaticData.non_existing_id.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
def test_CG8TC5_DELETE_verificar_status_code_OK_de_un_customer_group_utilizando_metodo_GET_en_lugar_de_DELETE(
        setup_function_customer_group):
    send_request_of_remove_customer_group(StaticData.group_id.value,None, Method.GET.value)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.functional
def test_CG8TC6_DELETE_verificar_la_eliminacion_de_un_customer_group_introduciendo_texto_en_lugar_de_id(
        setup_function_customer_group):
    send_request_of_remove_customer_group(StaticData.firstname.value)
    assert_response_status(TestData.response_status_code, 400)

@pytest.mark.regression
@pytest.mark.functional
def test_CG8TC7_DELETE_verificar_la_eliminacion_de_un_customer_group_con_simbolos_en_lugar_de_id(
        setup_function_customer_group):
    simbolos = Utils().get_random_symbols(5)
    send_request_of_remove_customer_group(simbolos, None)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG8TC8_DELETE_verificar_la_eliminacion_de_un_customer_group_con_id_vacio(setup_function_customer_group):
    send_request_of_remove_customer_group(StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG8TC9_DELETE_verificar_status_code_de_un_customer_group_utilizando_metodo_POST_en_lugar_de_DELETE(
        setup_function_customer_group):
    send_request_of_remove_customer_group(StaticData.group_id.value, None, Method.POST.value)
    assert_response_status(TestData.response_status_code, 404)