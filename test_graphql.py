from api.auth_http_methods import send_auth_post
from api.graphql_http_methods import send_get_device_type_post
from api.utils import get_access_token, get_response_dict, get_device_types
import pytest

# Testing a request for an access token
def test_auth_request(send_auth_post):
    assert send_auth_post.status_code == 200

# Testing a request to get a list of device types
def test_get_dev_types(get_access_token):
    dev_resp = send_get_device_type_post(get_access_token)
    assert dev_resp.status_code == 200
    deviceTypes = get_device_types(dev_resp)
    assert deviceTypes
