import pytest
import requests
from src.assertions.assertions_schema import assert_schemas
from src.assertions.assertions import assert_response_status
from src.enums.schema_json_name import SchemaName
from src.enums.static_data import StaticData
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from tests.helpers.utils import Utils
from tests.customer.setup import setup_function_customer
from tests.customer_group.setup import setup_module_customer_group, setup_function_customer_group
from src.testdata import TestData
from tests.customer.setup import send_request_obtener_customer_by_id, send_request_of_create_a_customer
from tests.customer_group.setup import send_request_of_update_customer_group_default, send_request_of_obtain_customer_group_by_id, send_request_of_create_a_customer_group, send_request_of_remove_customer_group
from src.enums.method import Method
from src.assertions.assertions import assert_equals



@pytest.mark.smoke
def test_CG03TC1_PUT_Asignacion_exitosa_de_Customer_Group_a_predeterminado(setup_module_customer_group):
    send_request_of_update_customer_group_default(TestData.module_response_json_customer_group["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
def test_CG03TC2_PUT_asignar_predeterminado_a_un_Customer_Group_ya_predeterminado(setup_module_customer_group):
    send_request_of_update_customer_group_default(1)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
def test_CG03TC3_PUT_Asignacion_de_Customer_Group_a_predeterminado_sin_token_de_autenticacion(setup_module_customer_group):
    send_request_of_update_customer_group_default(TestData.module_response_json_customer_group["id"], token=TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
def test_CG03TC4_PUT_Asignacion_de_Customer_Group_no_existente_a_predeterminado(setup_module_customer_group):
    send_request_of_update_customer_group_default(StaticData.non_existing_id.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.functional
def test_CG03TC5_PUT_Asignacion_de_Customer_Group_introduciendo_id_invalido_de_texto_a_predeterminado(setup_module_customer_group):
    send_request_of_update_customer_group_default(Utils.get_random_letters(5))
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG03TC6_PUT_Asignacion_de_Customer_Group_introduciendo_id_invalido_de_simbolos_a_predeterminado(setup_module_customer_group):
    send_request_of_update_customer_group_default(StaticData.symbols.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG03TC7_PUT_Asignacion_de_Customer_Group_introduciendo_id_invalido_vacio_a_predeterminado(setup_module_customer_group):
    send_request_of_update_customer_group_default(StaticData.empty_name.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG03TC8_PUT_Enviar_solicitud_GET_en_vez_de_PUT_para_actualizar_Customer_Group(setup_module_customer_group):
    send_request_of_update_customer_group_default(StaticData.empty_name.value, None, Method.GET.value)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.functional
def test_CG03TC9_PUT_Enviar_solicitud_DELETE_en_vez_de_PUT_para_actualizar_Customer_Group(setup_module_customer_group):
    send_request_of_update_customer_group_default(StaticData.empty_name.value, None, Method.DELETE.value)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.functional
def test_CG03TC10_PUT_Enviar_solicitud_POST_en_vez_de_PUT_para_actualizar_Customer_Group(setup_module_customer_group):
    send_request_of_update_customer_group_default(StaticData.empty_name.value, None, Method.POST.value)
    assert_response_status(TestData.response_status_code, 404)


@pytest.mark.regression
def test_CG03TC11_verificar_que_la_asignacion_de_un_customer_group_preterminado_no_afecta_obtener_customers_existentes_con_customer_group_no_predeterminados(setup_module_customer_group):
    send_request_of_update_customer_group_default(TestData.module_response_json_customer_group["id"])
    response_customer = send_request_obtener_customer_by_id(StaticData.customer_10.value)
    assert_equals(response_customer["id"], 10 )


@pytest.mark.functional
@pytest.mark.regression
def test_CG3TC12_PUT_validar_asignacion_customer_group_como_predeterminado_no_afecta_eliminacion_customer_group(setup_function_customer_group):
    response_json = send_request_of_update_customer_group_default(TestData.function_response_json_customer_group["id"])
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(response_json, SchemaName.put_customer_group_default.value)
    nuevo_customer_group = send_request_of_create_a_customer_group("grupo_para_eliminar")
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(nuevo_customer_group, SchemaName.post_customer_group.value)
    send_request_of_remove_customer_group(nuevo_customer_group["id"])
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.functional
@pytest.mark.regression
def test_CG3TC13_PUT_validar_asignacion_customer_group_como_predeterminado_no_afecta_creacion_customer(setup_function_customer_group, setup_function_customer):
    response_json = send_request_of_update_customer_group_default(TestData.function_response_json_customer_group["id"])
    assert_response_status(TestData.response_status_code, 200)
    assert_schemas(response_json, SchemaName.put_customer_group_default.value)
    nuevo_email = Utils.get_random_email()
    nuevo_customer = send_request_of_create_a_customer(nuevo_email,StaticData.firstname.value,StaticData.lastname.value)
    assert_response_status(TestData.response_status_code, 200)
    assert_equals(nuevo_customer[StaticData.group_id.name], TestData.function_response_json_customer_group["id"])
