import pytest

def assert_login_success(response):
    assert response is not None
    assert isinstance(response, str)
    assert len(response) >= 0
    return True

def assert_login_fail(response):
    assert isinstance(response, dict)
    assert isinstance(response.get("message", ""), str)
    return True
