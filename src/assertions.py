import requests

class Assertions:
    @staticmethod
    def assert_response_status(response: requests.Response, expected_status: int = 200):
        """Verifica que el código de estado de la respuesta sea el esperado."""
        assert response.status_code == expected_status, f"Expected status {expected_status}, got {response.status_code}"

    @staticmethod
    def assert_json_response(response: requests.Response):
        """Verifica que la respuesta sea un JSON válido y no sea None."""
        try:
            response_data = response.json()
        except ValueError:
            raise AssertionError("Response is not a valid JSON")
        assert response_data is not None, "Response JSON is None"
        return response_data

    @staticmethod
    def assert_json_keys(json_response, expected_keys):
        """Verifica que el JSON contenga las claves esperadas."""
        for key in expected_keys:
            assert key in json_response, f"Missing key: {key}"

    @staticmethod
    def assert_json_structure(json_response):
        """Verifica que la estructura del JSON sea la esperada."""
        expected_keys = ['id', 'code', 'tax_class_id', 'tax_class_name']
        assert isinstance(json_response, dict), "Response is not a dictionary"
        Assertions.assert_json_keys(json_response, expected_keys)
