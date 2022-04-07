import requests
import pytest
from api.utils import print_response, add_gdt_fields

dms_host_url = "https://device-model-service.dev.dt.conmob.cloud"
gdt_query_template = {"query":"query GetDeviceType {\r\n deviceTypes {}\r\n}","variables":{}}
gdt_query_fields = ["modelCode", "launchDate", "hardwareVersion"]

# Sending a request for a list of device types
def send_get_device_type_post(get_access_token) -> requests.Response:
    gdt_query = add_gdt_fields(gdt_query_template, gdt_query_fields)
    r = requests.post(url=dms_host_url + '/graphql', headers=get_access_token, json=gdt_query)
    print_response(r)
    return r