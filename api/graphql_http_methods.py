import requests
from api.utils import print_response, create_headers, get_str_fields, create_request_body

dms_host_url = "https://device-model-service.dev.dt.conmob.cloud"
variables = {}

gdt_query_fields_list = ["modelCode", "launchDate", "hardwareVersion"]
gdt_query_fields = get_str_fields(gdt_query_fields_list)
gdt_query = "query GetDeviceType {\r\n deviceTypes {" + ''.join(gdt_query_fields) + "}\r\n}"

gam_query_fields_list = ["id", "name", "revision"]
gam_query_fields = get_str_fields(gam_query_fields_list)
gam_query = "query GetAttributeModel {\r\n attributeModels {" + ''.join(gam_query_fields) + "}\r\n}"


# Sending a request for a list of device types
def send_get_device_type_post(get_access_token) -> requests.Response:
    headers = create_headers(get_access_token)
    body = create_request_body(gdt_query, variables)
    r = requests.post(url=dms_host_url + '/graphql', headers=headers, json=body)
    print_response(r)
    return r

# Sending a request for a list of attribute models
def send_get_attribute_model(get_access_token) -> requests.Response:
    headers = create_headers(get_access_token)
    body = create_request_body(gam_query, variables)
    r = requests.post(url=dms_host_url + '/graphql', headers=headers, json=body)
    print_response(r)
    return r