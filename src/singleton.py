import json
import os


class Singleton:
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
