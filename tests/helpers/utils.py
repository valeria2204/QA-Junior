import json
import os
import random
import string


class Utils:
    @staticmethod
    def read_schema_json_file(schema_json_name):
        file = open(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '\\src\\json_files\\schemas\\' + schema_json_name)
        data = json.load(file)
        return data


    @staticmethod
    def get_random_alphanumeric(length):
        characters = string.ascii_letters + string.digits
        return "".join(random.choices(characters, k=length))
    