import requests
import json

# Displaying information about a request
def print_response(response: requests.Response):
    # request
    print("\nSend {} {} HTTP {}".format(response.request.method, response.url, response.status_code))
    print("Request headers: \n{}".format(response.request.headers))
    print("Request body: {}".format(response.request.body))

    # response
    print("Response body: {}".format(response.text))

# Creating a dict for a request to get access token
def create_auth_data(grant_type: str, client_id: str, client_secret: str) -> dict:
    return {"grant_type": grant_type, "client_id": client_id, "client_secret": client_secret}

# Getting a token from a request response
def get_access_token(response: requests.Response) -> str:
    body_dict = json.loads(response.text)
    access_token = body_dict.get("access_token")
    return access_token

# Creating a header with an access token
def get_authorization_header(access_token: str) -> dict:
    header = {"Authorization": "Bearer " + access_token}
    return header