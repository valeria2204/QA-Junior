import json
import random
import pytest

from src.assertions.assertions import assert_response_status
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer_group.setup import send_request_of_create_a_customer_group

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC1_POST_Crear_nuevo_Customer_Group_con_informacion_basica_requerida(setup_data):
    numeroAleatorio= random.randint(0, 100)
    payload = json.dumps({
      "group": {
        "code": f"ney {numeroAleatorio}",
        "tax_class_id":3

      }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC2_POST_Crear_nuevo_Customer_Group_con_token_de_autentication_valida_y_con_body_vacio(setup_data):
    payload = json.dumps({})
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC3_POST_Crear_nuevo_Customer_Group_sin_token_de_autentication(setup_data):
    payload = json.dumps({
          "group": {
            "id": 100,
            "code": "NewYork",
            "tax_class_id": 1,
            "tax_class_name": "Arizona",
            "extension_attributes": {
              "exclude_website_ids": [
                0
          ]
        }
      }
    })
    send_request_of_create_a_customer_group({}, payload=payload, token="")
    assert_response_status(TestData.response_status_code, 401)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.skip(reason="error 500, error por identificar")
def test_CG1TC4_POST_Crear_nuevo_Customer_Group_con_todo_el_esquema_llenado(setup_data):
    numeroAleatorio = random.randint(0, 100)
    payload = json.dumps({
      "group": {
        "id": 100,
        "code": f"ney {numeroAleatorio}",
        "tax_class_id": 3,
        "tax_class_name": "Arizona",
        "extension_attributes": {
          "exclude_website_ids": [
            0
          ]
        }
      }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 200)



@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC5_POST_Crear_nuevo_Customer_Group_con_datos_invalidos_en_el_body(setup_data):
    payload = json.dumps(
    {"algun": "aleatorio"})
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 400)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC6_POST_Crear_nuevo_Customer_Group_con_campo_vacio_en_el_code(setup_data):
    payload = json.dumps({
      "group": {
        "code": "",
        "tax_class_id":3

      }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 400)
    assert "is required" in TestData.module_response_json["message"]

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC7_POST_Crear_nuevo_Customer_Group_con_un_string_en_tax_class_id(setup_data):
    payload = json.dumps({
        "group": {
            "code": "ejemplo",
            "tax_class_id": ""

        }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 400)
    assert "value's type is invalid" in TestData.module_response_json["message"]

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC8_POST_Crear_nuevo_Customer_Group_con_tax_class_id_no_valido(setup_data):
    numeroAleatorio = random.randint(1, 20)
    payload = json.dumps({
        "group": {
            "id": 1,
            "code": f"ney {numeroAleatorio}",
            "tax_class_id": 400,
        }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC9_POST_Crear_nuevo_Customer_Group_con_nombre_igual_a_100_caracteres(setup_data):
    texto_100_chars = "Lorem ipsun dolor sit amet, consectetur adipiscing elit. Ut consequat neque metus,.eu dapibus mi mi."
    payload = json.dumps({
        "group": {
            "id": 1,
            "code": texto_100_chars,
            "tax_class_id": 3,
        }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 200)
    assert len(texto_100_chars) == len(TestData.module_response_json["code"])


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC10_POST_Crear_nuevo_Customer_Group_con_nombre_igual_a_32_caracteres(setup_data):
    texto_32_chars = "Lorem ipsum dolor sit amet cras."
    payload = json.dumps({
        "group": {
            "id": 1,
            "code": texto_32_chars,
            "tax_class_id": 3,
        }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 200)
    assert len(texto_32_chars) == len(TestData.module_response_json["code"])

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CG1TC11_POST_Crear_nuevo_Customer_Group_con_caracteres_especiales(setup_data):
    texto_chars_especiales = "#$%&/()."
    payload = json.dumps({
        "group": {
            "id": 1,
            "code": texto_chars_especiales,
            "tax_class_id": 3,
        }
    })
    send_request_of_create_a_customer_group({}, payload=payload)
    assert_response_status(TestData.response_status_code, 200)
    assert len(texto_chars_especiales) == len(TestData.module_response_json["code"])