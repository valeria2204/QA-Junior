import json
import os


class TestData:
    __instance = None

    token = None
    username = None
    password = None
    token_all_access = None
    token_no_valid = None
    base_url = None

    response_json = None
    response_status_code = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = \
                super(TestData, cls).__new__(cls)



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
