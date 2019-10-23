import requests
import json
from app.forge.bim360team import bim360team
from app.forge.derivatives import derivatives
from app.forge.users import users

class api(object):
    _API_REALM = 'Autodesk Forge Authentication API'

    authentication_base_url = 'https://developer.api.autodesk.com/authentication'

    def __init__(self,
                 client_id=None,
                 client_secret=None,
                 grant_type=None,
                 scope=None,
                 code=None,
                 redirect_uri=None,
                 access_token=None,
                 refresh_token=None
                 ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._grant_type = grant_type
        self._scope = scope
        self._code = code
        self._redirect_uri = redirect_uri
        self._access_token = access_token
        self._refresh_token = refresh_token

    @property
    def derivatives(self):
        if self.is_valid_context():
            return derivatives(self, True)
        else:
            return derivatives(self, False)

    @property
    def bim360team(self):
        if self.is_valid_context():
            return bim360team(self, True)
        else:
            return bim360team(self, False)

    @property
    def users(self):
        if self.is_valid_context():
            return users(self, True)
        else:
            return users(self, False)

    def set_credentials(self, client_id=None, client_secret=None, grant_type=None, scope=None, code=None, redirect_uri=None, refresh_token=None, access_token=None):
        self._client_id = client_id
        self._client_secret = client_secret
        self._grant_type = grant_type
        self._scope = scope
        self._code = code
        self._redirect_uri = redirect_uri
        self._refresh_token = refresh_token
        self._access_token = access_token
        return self

    def get_credentials(self):
        return {'client_id': self._client_id,
                'client_secret': self._client_secret,
                'grant_type': self._grant_type,
                'scope': self._scope,
                'code': self._code,
                'redirect_uri': self._redirect_uri,
                'refresh_token': self._refresh_token,
                'access_token': self._access_token
        }

    def retrieve_token_2leg(self):
        if not all([self._client_id, self._client_secret, self._grant_type, self._scope]):
            raise Exception('Please check that credentials are set - See: api.set_credentials()')

        token_endpoint = 'v1/authenticate'
        get_token_url = "/".join([self.authentication_base_url, token_endpoint])

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = [
            ('client_id', self._client_id),
            ('client_secret', self._client_secret),
            ('grant_type', self._grant_type),
            ('scope', self._scope),
        ]

        response = requests.post(get_token_url, headers=headers, data=data)
        response_object = response.json()
        return response_object

    def retrieve_token_3leg(self):
        if not all([self._client_id, self._client_secret, self._grant_type, self._code, self._redirect_uri]):
            raise Exception('Please check that credentials are set - See: api.set_credentials() - 3Leg authentication also requires code and redirect_uri parameters')

        token_endpoint = 'v1/gettoken'
        get_token_url = "/".join([self.authentication_base_url, token_endpoint])

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = [
            ('client_id', self._client_id),
            ('client_secret', self._client_secret),
            ('grant_type', self._grant_type),
            ('code', self._code),
            ('redirect_uri', self._redirect_uri)
        ]

        response = requests.post(get_token_url, headers=headers, data=data)
        response_object = response.json()
        return response_object

    def is_valid_context(self):
        if self._access_token:
            return True
        else:
            return False

    def get_refreshed_token(self):
        if not all([self._client_id, self._client_secret, self._grant_type]):
            raise Exception('Please check that credentials are set - See: api.set_credentials() - 3Leg authentication also requires code and redirect_uri parameters')

        token_endpoint = 'v1/refreshtoken'
        get_token_url = "/".join([self.authentication_base_url, token_endpoint])

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = [
            ('client_id', self._client_id),
            ('client_secret', self._client_secret),
            ('grant_type', self._grant_type),
            ('refresh_token', self._refresh_token)
        ]

        response = requests.post(get_token_url, headers=headers, data=data)
        return response.json()