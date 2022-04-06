from api.http_methods import send_auth_post, send_get_device_type_post
from api.utils import get_access_token

token_host_url = "https://keycloak.dev.iat.conmob.cloud/auth/realms/sso/protocol/openid-connect/token"
dms_host = "https://device-model-service.dev.dt.conmob.cloud"
grant_type = "client_credentials"
client_id = "device-model-ui"
client_secret = "5MJaGE3H2FMcTGhGqDESCfP6ovTPvPKz"
get_dev_types_query = {"query":"query GetDeviceType {\r\n deviceTypes {\r\n id\r\n modelCode\r\n launchDate\r\n hardwareVersion\r\n protocolName\r\n protocolVersion\r\n xtu\r\n }\r\n}","variables":{}}

# Testing a request for an access token
def test_auth_request():

    response = send_auth_post(token_host_url, grant_type, client_id, client_secret)
    assert response.status_code == 200

# Testing a request to get a list of device types
def test_get_dev_types():

    auth_resp = send_auth_post(token_host_url, grant_type, client_id, client_secret)
    access_token = get_access_token(auth_resp)
    dev_resp = send_get_device_type_post(dms_host, access_token, get_dev_types_query)
    assert dev_resp.status_code == 200

