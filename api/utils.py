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
    header = {"Authorization": "Bearer " + access_token}
    return header

# Adding fields to a query
def add_gdt_fields(gdt_query: dict, fields: list) -> dict:
    queryField = gdt_query.get("query")
    dt_fields = get_str_fields(fields)
    dt_fields_ind = queryField.index("}")
    fullQueryField = f'{queryField[:dt_fields_ind]}{dt_fields}{queryField[dt_fields_ind:]}'
    gdt_query["query"] = fullQueryField
    return gdt_query

# Getting query fields as a string
def get_str_fields(fields: list) -> str:
    str_fields = ''
    for field in fields:
        str_fields += '\r\n ' + field
    str_fields += '\r\n '
    return str_fields

# Getting response dict data
def get_response_dict(response: requests.Response) -> dict:
    return json.loads(response.text)

# Getting device types data from response
def get_device_types(response: requests.Response) -> dict:
    resp_dict_data = get_response_dict(response)
    try:
        deviceTypes = resp_dict_data.get("data").get("deviceTypes")
    except AttributeError:
        deviceTypes = {}
    return deviceTypes