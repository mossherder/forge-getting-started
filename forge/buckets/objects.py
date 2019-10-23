import requests
import urllib.parse

def get_bucket_objects(authorization, bucket_key):
    headers = {
        'Authorization': authorization,
    }
    base_endpoint = 'https://developer.api.autodesk.com/oss/v2/buckets/'
    bucket_objects = '{0}/objects'.format(bucket_key)
    bucket_endpoint = urllib.parse.urljoin(base_endpoint, bucket_objects)
    response = requests.get(bucket_endpoint, headers=headers)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJBTFlKNlg1amhOTDdZNkNNUGxraDVRWGpLRkZwWVFIWiIsImV4cCI6MTUzMDY0ODY4OSwic2NvcGUiOlsiZGF0YTpyZWFkIiwidmlld2FibGVzOnJlYWQiLCJhY2NvdW50OnJlYWQiXSwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoiNHJKVFo4SGl1YjhxV2NTRGs4YXl0dE1yUUh4bFQ4N2R1MzkxaUJSMjZuR2M3UHpBUlZ5RFc4N1NydVh2M2plZyJ9.pJLb5iI5fdGwdI4_-NtchMS77XbSiz6STNwPqvsk0LA'
bucket_key = "firstbucketmossherder"
get_bucket_objects_response = get_bucket_objects(authorization, bucket_key)
print(get_bucket_objects_response.text)