from api.http_methods import send_auth_post

hostname_url = "https://keycloak.dev.iat.conmob.cloud/auth/realms/sso/protocol/openid-connect/token"
grant_type = "client_credentials"
client_id = "device-model-ui"
client_secret = "5MJaGE3H2FMcTGhGqDESCfP6ovTPvPKz"

def test_auth_request():

    response = send_auth_post(hostname_url, grant_type, client_id, client_secret)
    assert response.status_code == 200