import requests
from api.utils import print_response, create_headers, create_request_body

dms_host_url = "https://device-model-service.dev.dt.conmob.cloud"
variables = {}

# Sending a request for a list of device types
def send_get_device_type(get_access_token, gdt_query_fields=["modelCode ", "launchDate ", "hardwareVersion"]) -> requests.Response:
    headers = create_headers(get_access_token)
    gdt_query = "query GetDeviceType {\r\n deviceTypes {" + ''.join(gdt_query_fields) + "}\r\n}"
    body = create_request_body(gdt_query, variables)
    r = requests.post(url=dms_host_url + '/graphql', headers=headers, json=body)
    print_response(r)
    return r

# Sending a request for a list of attribute models
def send_get_attribute_model(get_access_token, gam_query_fields=["id ", "name ", "revision"]) -> requests.Response:
    headers = create_headers(get_access_token)
    gam_query = "query GetAttributeModel {\r\n attributeModels {" + ''.join(gam_query_fields) + "}\r\n}"
    body = create_request_body(gam_query, variables)
    r = requests.post(url=dms_host_url + '/graphql', headers=headers, json=body)
    print_response(r)
    return r