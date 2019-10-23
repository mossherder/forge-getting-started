import requests
import urllib

def get_guid_objects(authorization, urn, guid):
    headers = {
        'Authorization': authorization,
    }

    base_endpoint = 'https://developer.api.autodesk.com/modelderivative/v2/designdata'
    urn_metadata = '{0}/metadata'.format(urn)
    guid_properties = '{0}'.format(guid)
    guid_properties_endpoint = "/".join([base_endpoint, urn_metadata, guid_properties])

    response = requests.get(guid_properties_endpoint, headers=headers)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJ1c2VyaWQiOiJEVTNOUlZITEc0TkoiLCJleHAiOjE1MzA2NTI0NjYsInNjb3BlIjpbImRhdGE6Y3JlYXRlIiwiZGF0YTp3cml0ZSIsImRhdGE6cmVhZCIsImJ1Y2tldDpyZWFkIiwiYnVja2V0OnVwZGF0ZSIsImJ1Y2tldDpjcmVhdGUiLCJ2aWV3YWJsZXM6cmVhZCJdLCJjbGllbnRfaWQiOiJBTFlKNlg1amhOTDdZNkNNUGxraDVRWGpLRkZwWVFIWiIsImdyYW50X2lkIjoibVNRQ2NjbzMxaDZPR1hWQzVaOUtYZVZRc0VwN2s2NG0iLCJhdWQiOiJodHRwczovL2F1dG9kZXNrLmNvbS9hdWQvand0ZXhwNjAiLCJqdGkiOiJkTTdEbGdPMnA3NnNhZW5PRjFuQmJzUkxYSGZQdWRYZnFNMVc0RTBwVk5NcTU2aWZzbHRrUWg5WEE1WUQyYzdmIn0.4zBHKPxymHD7f4S1EdGy3MVqgRgcwG-UKg8wVqk1aoo'
urn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6d2lwLmRtLnByb2QvNGJjMGE1NzQtMzk1NS00OWJmLTljMWEtMjk5Mzg0NWI2NDRkLnJ2dA'
guid = "c3ed66e5-b5b6-4fd6-88f7-543bc24b6b83"
properties_response = get_guid_objects(authorization, urn, guid)
print(properties_response.text)
