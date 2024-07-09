import requests

from src.request_library.actions import Actions


class RequestModule(Actions):

    def __init__(self, method_name, url, headers, payload, params):
        self.method_name = method_name
        self.url = url
        self.headers = headers
        self.payload = payload
        self.params = params

    def run(self):
        return requests.request(self.method_name, self.url, headers=self.headers, data=self.payload, params=self.params)
