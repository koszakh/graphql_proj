import requests
import json
import pytest

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
@pytest.fixture
@pytest.mark.usefixtures("send_auth_post")
def get_access_token(send_auth_post) -> str:
    body_dict = json.loads(send_auth_post.text)
    access_token = body_dict.get("access_token")
    header_auth = {"Authorization": "Bearer " + access_token}
    return header_auth

# Creating headers for a request
def create_headers(access_token) -> dict:
    headers = {"Accept":"", "Content-type":"application/json","Authorization":access_token["Authorization"]}
    return headers

# Creating a request body
def create_request_body(query: str, variables: str) -> dict:
    body = {"query":query, "variables":variables}
    return body

# Getting response dict data
def get_response_dict(response: requests.Response) -> dict:
    return json.loads(response.text)

# Getting device types data from response
def get_device_types(response: requests.Response) -> dict:
    resp_dict_data = get_response_dict(response)
    try:
        deviceTypes = resp_dict_data.get("data").get("deviceTypes")
    except AttributeError:
        deviceTypes = None
    return deviceTypes

# Getting attribute models data from response
def get_attribute_models(response: requests.Response) -> dict:
    resp_dict_data = get_response_dict(response)
    try:
        attributeModels = resp_dict_data.get("data").get("attributeModels")
    except AttributeError:
        attributeModels = None
    return attributeModels