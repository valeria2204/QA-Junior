import requests
import jsonschema
import pytest
from src.singleton import Singleton


def assert_response_status(actual_status_code, expected_status):
    """Verifica que el código de estado de la respuesta sea el esperado."""
    assert actual_status_code == expected_status, f"Expected status {expected_status}, got {actual_status_code}"

