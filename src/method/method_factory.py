from src.method.python_requests_module import HTTPRequest


class MethodFactory:

    def create_request(self, name, method_name, url, headers, payload, params):
        if name == 'http_request':
            return HTTPRequest(method_name, url, headers, payload, params)
