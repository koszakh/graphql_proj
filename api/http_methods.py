import requests
from api.utils import create_auth_data, print_response, get_authorization_header

# Sending a request for a access token
def send_auth_post(host: str, grant_type: str, client_id: str, client_secret: str) -> requests.Response:
    data_dict = create_auth_data(grant_type, client_id, client_secret)
    r = requests.post(url=host, data=data_dict)
    print_response(r)
    return r

# Sending a request for a list of device types
def send_get_device_type_post(host: str, access_token: str, query: dict) -> requests.Response:
    auth_header = get_authorization_header(access_token)
    r = requests.post(url=host + '/graphql', headers=auth_header, json=query)
    print_response(r)
    return r