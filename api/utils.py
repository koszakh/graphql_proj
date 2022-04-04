import requests

# Displaying information about a request
def print_response(response: requests.Response):
    # request
    print("\nSend {} {} HTTP {}".format(response.request.method, response.url, response.status_code))
    print("Request headers: \n{}".format(response.request.headers))
    print("Request body: {}".format(response.request.body))

    # response
    print("Response body: {}".format(response.text))

def create_auth_data(grant_type: str, client_id: str, client_secret: str):

    return {"grant_type": grant_type, "client_id": client_id, "client_secret": client_secret}