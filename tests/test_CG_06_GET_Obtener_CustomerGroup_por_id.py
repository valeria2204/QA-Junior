import pytest
import requests
import jsonschema
from src.singleton import Singleton


# CG-06-TC1: [GET] Verificar obtención exitosa de un grupo de clientes por ID
@pytest.mark.smoke
def test_CG_06_TC1_GET_verificar_obtencion_exitosa_de_un_grupo_de_clientes_por_id(get_token_login):
    group_id = 1  # ID válido de un grupo de clientes existente

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    headers = {
        'Authorization':