import requests
import urllib

def get_folder_contents(authorization, project_id, folder_id):
    headers = {
        'Authorization': authorization,
    }

    base_endpoint = 'https://developer.api.autodesk.com/data/v1/projects'
    project_folders = '{0}/folders'.format(project_id)
    folder_contents = '{0}/contents'.format(folder_id)
    project_contents_endpoint = "/".join([base_endpoint, project_folders, folder_contents])

    response = requests.get(project_contents_endpoint, headers=headers)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJ1c2VyaWQiOiJEVTNOUlZITEc0TkoiLCJleHAiOjE1MzA2NDkxMTgsInNjb3BlIjpbImRhdGE6Y3JlYXRlIiwiZGF0YTp3cml0ZSIsImRhdGE6cmVhZCIsImJ1Y2tldDpyZWFkIiwiYnVja2V0OnVwZGF0ZSIsImJ1Y2tldDpjcmVhdGUiXSwiY2xpZW50X2lkIjoiQUxZSjZYNWpoTkw3WTZDTVBsa2g1UVhqS0ZGcFlRSFoiLCJncmFudF9pZCI6Im5rWjBRalNOS1JIaTFhZlMycWZJYmZPanJOaHEyeldiIiwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoibmowQ2phd1lETDM0OE9qR1p3V09VU1d0MmpGMkZDYTBuQ0JOZkNxcXJ1bjUwb1RNR2hleFlLTm8yajE1dVA3byJ9.m25axEwKF4vqxDbBXy7mrqoxajTjR7pO21jUtFFFf1U'
project_id = "a.YnVzaW5lc3M6ZmFpdGh0ZWNobm9sb2dpZXM2IzIwMTgwNTAxMTMwMDQzNjAx"
folder_id = "urn:adsk.wipprod:fs.folder:co.lyOleuWqRCyg5m467mKNxg"
contents_response = get_folder_contents(authorization, project_id, folder_id)
print(contents_response.text)