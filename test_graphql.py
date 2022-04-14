import pytest
from api.graphql_http_methods import send_get_device_type_post, send_get_attribute_model
from api.utils import get_device_types, get_attribute_models

# Testing a request for an access token
def test_auth_request(send_auth_post):
    assert send_auth_post.status_code == 200

# Testing a request to get a list of device types
def test_get_dev_types(get_access_token):
    dev_resp = send_get_device_type_post(get_access_token)
    assert dev_resp.status_code == 200
    deviceTypes = get_device_types(dev_resp)
    assert isinstance(deviceTypes, list)

# Testing a request to get a list of attribute models
def test_get_attr_model(get_access_token):
    attr_resp = send_get_attribute_model(get_access_token)
    assert attr_resp.status_code == 200
    attributeModels = get_attribute_models(attr_resp)
    assert isinstance(attributeModels, list)
