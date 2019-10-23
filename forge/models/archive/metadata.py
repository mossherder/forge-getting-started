import requests
import urllib
def get_metadata(authorization, urn):
    headers = {
        'Authorization': authorization,
    }

    base_endpoint = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/'
    urn_metadata = '{0}/metadata'.format(urn)
    metadata_endpoint = urllib.parse.urljoin(base_endpoint, urn_metadata)

    response = requests.get(metadata_endpoint, headers=headers)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJ1c2VyaWQiOiJEVTNOUlZITEc0TkoiLCJleHAiOjE1MzA2NDkxMTgsInNjb3BlIjpbImRhdGE6Y3JlYXRlIiwiZGF0YTp3cml0ZSIsImRhdGE6cmVhZCIsImJ1Y2tldDpyZWFkIiwiYnVja2V0OnVwZGF0ZSIsImJ1Y2tldDpjcmVhdGUiXSwiY2xpZW50X2lkIjoiQUxZSjZYNWpoTkw3WTZDTVBsa2g1UVhqS0ZGcFlRSFoiLCJncmFudF9pZCI6Im5rWjBRalNOS1JIaTFhZlMycWZJYmZPanJOaHEyeldiIiwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoibmowQ2phd1lETDM0OE9qR1p3V09VU1d0MmpGMkZDYTBuQ0JOZkNxcXJ1bjUwb1RNR2hleFlLTm8yajE1dVA3byJ9.m25axEwKF4vqxDbBXy7mrqoxajTjR7pO21jUtFFFf1U'
urn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6d2lwLmRtLnByb2QvNGJjMGE1NzQtMzk1NS00OWJmLTljMWEtMjk5Mzg0NWI2NDRkLnJ2dA'
metadata_response = get_metadata(authorization, urn)
print(metadata_response.text)
