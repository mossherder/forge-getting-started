import requests
import json
import base64

class derivatives(object):
    _API_REALM = 'Autodesk Forge Model Derivative API'

    derivatives_base_url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata'

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

    def get_guid(self, urn, model_guid):
        urn_metadata = '{0}/metadata'.format(urn)
        guid = '{0}'.format(model_guid)
        guid_endpoint = "/".join([self.derivatives_base_url, urn_metadata, guid_properties])

        response = requests.get(guid_properties_endpoint, headers=self._headers)
        return response.json()

    def get_guid_properties(self, urn, model_guid):
        urn_metadata = '{0}/metadata'.format(urn)
        guid_properties = '{0}/properties'.format(model_guid)
        guid_properties_endpoint = "/".join([self.derivatives_base_url, urn_metadata, guid_properties])

        response = requests.get(guid_properties_endpoint, headers=self._headers)
        return response.json()

    def get_metadata(self, urn):
        urn_metadata = '{0}/metadata'.format(urn)
        metadata_endpoint = "/".join([self.derivatives_base_url, urn_metadata])

        response = requests.get(metadata_endpoint, headers=self._headers)
        return response.json()

    def translate_urn(self, urn, to_type, view_types, region):
        data = {
            "input": {
                "urn": urn,
            },
            "output": {
                "destination": {
                    "region": region
                },
                "formats": [
                    {
                        "type": to_type,
                        "views": view_types
                    },
                ]
            }
        }

        translate_endpoint = "/".join([self.derivatives_base_url, 'job'])

        response = requests.post('https://developer.api.autodesk.com/modelderivative/v2/designdata/job' , data=json.dumps(data), headers=self._headers)
        return response.json()

    def verify_manifest(self, urn):
        urn_metadata = '{0}/manifest'.format(urn)
        verify_endpoint = "/".join([self.derivatives_base_url, urn_metadata])
        manifest_response = requests.get(verify_endpoint, headers=self._headers)
        return manifest_response.json()

    def is_access_token_valid(self):
        response = requests.get('https://developer.api.autodesk.com/modelderivative/v2/designdata/formats', headers=self._headers)
        return response.status_code == 200

    @staticmethod
    def urn_to_base64(urn):
        return base64.b64encode(urn.encode()).rstrip(b'=').decode()