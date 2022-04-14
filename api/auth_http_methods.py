import pytest
import requests
from api.utils import create_auth_data, print_response

token_host_url = "https://keycloak.dev.iat.conmob.cloud/auth/realms/sso/protocol/openid-connect/token"
grant_type = "client_credentials"
client_id = "device-model-ui"
client_secret = "5MJaGE3H2FMcTGhGqDESCfP6ovTPvPKz"

# Sending a request for an access token
@pytest.fixture
def send_auth_post() -> requests.Response:
    data_dict = create_auth_data(grant_type, client_id, client_secret)
    r = requests.post(url=token_host_url, data=data_dict)
    print_response(r)
    return r
