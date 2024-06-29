def assert_unauthorized_response(response):
    assert response.status_code == 401
    response_data = response.json()
    assert "message" in response_data
    assert response_data["message"].startswith("The consumer isn't authorized to access")
    assert "parameters" in response_data
    assert "resources" in response_data["parameters"]
    assert response_data["parameters"]["resources"] == "Magento_Customer::group"
