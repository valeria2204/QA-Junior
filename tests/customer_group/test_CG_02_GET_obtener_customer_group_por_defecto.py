import pytest

from src.assertions.assertions import assert_response_status
from src.assertions.assertions_schema import assert_schemas
from src.testdata import TestData
from tests.conftest import setup_data, send_request_of_obtain_default_customer_group_by


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG2TC1_GET_verificar_la_obtencion_exitosa_de_customer_groups_por_defecto(setup_data):
    send_request_of_obtain_default_customer_group_by()
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG2TC2_GET_verificar_esquema_obtencion_exitosa_de_customer_groups_por_defecto(setup_data):
    send_request_of_obtain_default_customer_group_by()
    assert_schemas(TestData.response_json, 'get_customer_group.json')


@pytest.mark.regression
@pytest.mark.functional
def test_CG2TC3_GET_verificar_que_retorna_una_respuesta_401_al_obtener_el_customer_groups_por_defecto_cuando_no_tiene_un_token_valido(setup_data):
    send_request_of_obtain_default_customer_group_by(TestData.token_no_valid)
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.regression
def test_CG2TC4_GET_verificar_que_retorna_una_respuesta_401_al_obtener_el_customer_groups_por_defecto_cuando_no_tiene_un_header_authorization(setup_data):
    send_request_of_obtain_default_customer_group_by(TestData.token, {})
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.functional
@pytest.mark.regression
def test_CG2TC5_GET_verificar_la_obtencion_de_el_customer_groups_por_defecto_tenga_el_id_de_tipo_numero_entero_positivo(setup_data):
    send_request_of_obtain_default_customer_group_by()

    assert_response_status(TestData.response_status_code, 200)
    assert isinstance(TestData.response_json["id"], int)
    assert TestData.response_json["id"] >= 0


@pytest.mark.functional
@pytest.mark.regression
def test_CG2TC6_GET_verificar_la_obtencion_de_el_customer_groups_por_defecto_tenga_el_class_id_de_tipo_numero_entero_positivo(setup_data):
    send_request_of_obtain_default_customer_group_by()

    assert_response_status(TestData.response_status_code, 200)
    assert isinstance(TestData.response_json["tax_class_id"], int)
    assert TestData.response_json["tax_class_id"] >= 0


@pytest.mark.regression
def test_CG2TC7_GET_verificar_la_obtencion_de_el_customer_groups_por_defecto_tenga_el_valor_de_code_no_vacio(setup_data):
    send_request_of_obtain_default_customer_group_by()

    assert_response_status(TestData.response_status_code, 200)
    assert isinstance(TestData.response_json["code"], str)
    assert len(TestData.response_json["code"]) >= 0


@pytest.mark.regression
def test_CG2TC8_GET_verificar_la_obtencion_de_el_customer_groups_por_defecto_tenga_el_valor_de_tax_class_name_no_vacio(setup_data):
    send_request_of_obtain_default_customer_group_by()

    assert isinstance(TestData.response_json["tax_class_name"], str)
    assert len(TestData.response_json["tax_class_name"]) >= 0


@pytest.mark.regression
def test_CG2TC9_GET_verificar_la_obtencion_de_el_customer_groups_por_defecto_no_se_ve_afectado_cuando_se_envia_un_parametro_de_consulta(setup_data):
    send_request_of_obtain_default_customer_group_by(None, None, None, "?code=LoremIpsum")

    assert_response_status(TestData.response_status_code, 200)
    assert TestData.response_json["id"] == 1
