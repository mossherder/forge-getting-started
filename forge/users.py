import requests
import json

class users(object):
    _API_REALM = 'Autodesk Forge BIM360 Team API'

    users_base_url = 'https://developer.api.autodesk.com/userprofile/v1/users'

    def __init__(self, api, is_api_valid):
        self._api = api
        self._is_api_valid = is_api_valid
        if is_api_valid:
            bearer_key = ' '.join(['Bearer', api._access_token])
            self._headers = headers = {
                                'Authorization': bearer_key,
                                'Content-Type': 'application/json'
                                }
        else:
            self._headers = None

    def get_end_user(self):
        me_endpoint = '@me'
        end_user_endpoint = "/".join([self.users_base_url, me_endpoint])

        response = requests.get(end_user_endpoint, headers=self._headers)
        return response.json()

    def is_access_token_valid(self):
        me_endpoint = '@me'
        end_user_endpoint = "/".join([self.users_base_url, me_endpoint])

        response = requests.get(end_user_endpoint, headers=self._headers)
        return response.status_code == 200