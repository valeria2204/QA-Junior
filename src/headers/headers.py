def header_content_type(content_type="application/json"):
    headers = {'Content-Type': f'{content_type}'}
    return headers


def header_content_type_authorization(bearer_token, content_type="application/json"):
    headers = {
        'Content-Type': f'{content_type}',
        'Authorization': f'Bearer {bearer_token}',
    }
    return headers


def header_authorization(bearer_token):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
    }
    return headers
