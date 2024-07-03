import requests
import jsonschema
import pytest
from src.testdata import TestData


def assert_response_status(actual_status_code, expected_status):
    assert actual_status_code == expected_status, f"Expected status {expected_status}, got {actual_status_code}"

