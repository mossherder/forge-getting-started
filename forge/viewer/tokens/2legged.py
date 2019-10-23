import requests

#Makes an access token request
def retrieve_token(client_id, client_secret, grant_type, scope):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = [
        ('client_id', client_id),
        ('client_secret', client_secret),
        ('grant_type', grant_type),
        ('scope', scope),
    ]
    response = requests.post('https://developer.api.autodesk.com/authentication/v1/authenticate', headers=headers, data=data)
    return response

client_id = 'ZaG1pdO7yNDzbgGFAUmkflDeDloDaRP4'
secret = 'kMPN3imZjhWd5LEJ'
grant_type = 'client_credentials'
scope ='bucket:create data:read viewables:read account:read data:create'
token_request_response = retrieve_token(client_id, secret, grant_type, scope).json()
print(' '.join([token_request_response["token_type"], token_request_response["access_token"]]))