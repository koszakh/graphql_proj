import requests
from api.utils import create_auth_data, print_response

def send_auth_post(host: str, grant_type: str, client_id: str, client_secret: str) -> requests.Response:

    data_dict = create_auth_data(grant_type, client_id, client_secret)
    r = requests.post(url=host, data=data_dict)
    print_response(r)
    return r