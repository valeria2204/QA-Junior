import json
import os
import string
import random


class Singleton:
    response_404_json = None
    response_404_status_code = None
    response_400_json = None
    response_400_status_code = None
    response_401_json = None
    response_401_status_code = None

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = \
                super(Singleton, cls).__new__(cls)

        return cls.__instance

    @staticmethod
    def get_username():
        file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\credentials.json')
        data = json.load(file)
        return data['username']

    @staticmethod
    def get_password():
        file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\credentials.json')
        data = json.load(file)
        return data['password']

    @staticmethod
    def get_base_url():
        file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\credentials.json')
        data = json.load(file)
        return data['base_url']

    @staticmethod
    def read_schema_json_file(schema_json_name):
        file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\schemas\\' + schema_json_name)
        data = json.load(file)
        return data

    @staticmethod
    def get_random_alphanumeric(length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))


    @staticmethod
    def get_token_no_valid():
        file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\credentials.json')
        data = json.load(file)
        return data['token_no_valid']


    @staticmethod
    def get_token_all_access():
        file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\credentials.json')
        data = json.load(file)
        return data['token_all_access']