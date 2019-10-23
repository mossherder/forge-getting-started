import requests

def gen_callback_auth(client_id, redirect_url):

    base_endpoint = "https://developer.api.autodesk.com/authentication/v1/authorize?response_type=token&client_id=" + client_id + "&redirect_uri=" + redirect_url + "&scope=data:read"

    return base_endpoint

print(gen_callback_auth('ALYJ6X5jhNL7Y6CMPlkh5QXjKFFpYQHZ', "%0D%0Ahttps%3A%2F%2Fwww.evolvebim.com%2F"))