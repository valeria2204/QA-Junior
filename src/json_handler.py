import os
import json

def read_json(schema_json_name):
    file = open(os.path.dirname(os.path.abspath(__file__)) + '\\json_files\\schemas\\' + schema_json_name)
    data = json.load(file)
    return data
