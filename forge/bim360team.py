import requests
import json

class bim360team(object):
    _API_REALM = 'Autodesk Forge BIM360 Team API'

    bim360team_base_url = 'https://developer.api.autodesk.com/project/v1/hubs'
    bim360team_projects_base_url = 'https://developer.api.autodesk.com/data/v1/projects' #projects endpoint is diff /shrug

    def __init__(self, api, is_api_valid):
        self._api = api
        self._is_api_valid = is_api_valid
        if is_api_valid:
            bearer_key = ' '.join(['Bearer', api._access_token])
            self._headers = headers = {
                                'Authorization': bearer_key,
                                }
        else:
            self._headers = None

    def get_folder_contents(self, project_id, folder_id):
        project_folders = '{0}/folders'.format(project_id)
        folder_contents = '{0}/contents'.format(folder_id)
        folder_contents_endpoint = "/".join([self.bim360team_projects_base_url, project_folders, folder_contents])

        response = requests.get(folder_contents_endpoint, headers=self._headers)
        return response.json()

    def get_hubs(self):
        response = requests.get(self.bim360team_base_url, headers=self._headers)
        return response.json()

    def get_projects(self, hub_id):
        hub_projects = '{0}/projects'.format(hub_id)
        projects_endpoint = "/".join([self.bim360team_base_url, hub_projects])
        response = requests.get(projects_endpoint, headers=self._headers)
        return response.json()

    def get_folders(self, hub_id, project_id):
        hubs = '{0}/projects'.format(hub_id)
        project_folders = '{0}/topFolders'.format(project_id)
        folders_endpoint = "/".join([self.bim360team_base_url, hubs, project_folders])
        response = requests.get(folders_endpoint, headers=self._headers)
        return response.json()

    def get_folder_contents(self, project_id, folder_id):
        project_folders = '{0}/folders'.format(project_id)
        folder_contents = '{0}/contents'.format(folder_id)
        folders_endpoint = "/".join([self.bim360team_projects_base_url, project_folders, folder_contents])
        response = requests.get(folders_endpoint, headers=self._headers)
        return response.json()

    def get_item_versions(self, project_id, item_id):
        project = '{0}/items'.format(project_id)
        item_versions = '{0}/versions'.format(item_id)
        item_verions_endpoint = "/".join([self.bim360team_projects_base_url, project, item_versions])
        response = requests.get(item_verions_endpoint, headers=self._headers)
        return response.json()

    def is_access_token_valid(self):
        response = requests.get(self.bim360team_base_url, headers=self._headers)
        return response.status_code == 200