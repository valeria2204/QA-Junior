import json
import os

from src.method.method_factory import MethodFactory


class TestData:
    module_response_json = None
    function_response_json = None

    __instance = None

    token = None
    username = None
    password = None
    token_all_access = None
    token_no_valid = None
    base_url = None

    response_status_code = None
    old_password = None
    random_email = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = \
                super(TestData, cls).__new__(cls)

    @staticmethod
    def request_client(method_name, url, headers=None, payload=None, params=None):
        if params is None:
            params = {}
        if payload is None:
            payload = {}
        if headers is None:
            headers = {}
        request_factory = MethodFactory()
        return request_factory.create_request('http_request', method_name, url, headers, payload, params)

    @staticmethod
    def load_attributes_from_json():
        if TestData.token is None:
            file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\credentials.json')
            data = json.load(file)
            TestData.username = data['username']
            TestData.password = data['password']
            TestData.token_all_access = data['token_all_access']
            TestData.base_url = data['base_url']
            TestData.token_no_valid = data['token_no_valid']
