from src.request_library.requests_module import RequestModule


class MethodFactory:

    def create_request(self, name, method_name, url, headers, payload, params):
        if name == 'http_request':
            return RequestModule(method_name, url, headers, payload, params)
