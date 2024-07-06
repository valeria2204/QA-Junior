import datetime
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


    @staticmethod
    def get_random_email():
        characters = string.ascii_letters + string.digits
        return "".join(random.choices(characters, k=6))+"@gmail.com"


    @staticmethod
    def get_random_numerics(length):
        return "".join(random.choices(string.digits, k=length))


    @staticmethod
    def get_random_letters(length):
        return "".join(random.choices(string.ascii_letters, k=length))


    @staticmethod
    def get_random_symbols(length):
        return "".join(random.choices(string.punctuation, k=length))


    @staticmethod
    def random_past_date(start=datetime.datetime(2000, 1, 1), end=datetime.datetime.now()):
        return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


    @staticmethod
    def random_future_date(start=datetime.datetime.now(), end=datetime.datetime(3000, 1, 1)):
        return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


    @staticmethod
    def random_current_date():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    @staticmethod
    def get_random_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=length))
        password = password.replace('~', "")
        return "".join(password)

