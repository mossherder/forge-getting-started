import requests
import urllib.parse

def upload_to_bucket(authorization, bucket_key, object_name, file_path):
    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/octet-stream'
        #'Content-Length': '308331', #May or may not need to add this
    }
    #"C:\Users\mmendez\Vision Projects\Configurator\excellerate-configurator-resources\AssemblyConfigurationTestProject.rvt"
    with open(file_path, 'rb') as files:
        base_endpoint = 'https://developer.api.autodesk.com/oss/v2/buckets/'
        bucket_object = '{0}/objects/{1}'.format(bucket_key, object_name)
        object_endpoint = urllib.parse.urljoin(base_endpoint, bucket_object)
        response = requests.put(object_endpoint, headers=headers, data=files)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJaYUcxcGRPN3lORHpiZ0dGQVVta2ZsRGVEbG9EYVJQNCIsImV4cCI6MTUzNzgxMDI1MCwic2NvcGUiOlsiYnVja2V0OmNyZWF0ZSIsImRhdGE6cmVhZCIsInZpZXdhYmxlczpyZWFkIiwiYWNjb3VudDpyZWFkIiwiZGF0YTpjcmVhdGUiXSwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoiMXkwWE5Sb29sZVNmU3g3VXY3NnZHNU9ueUJLUXhqQUU4akdRQ0pBN3M1bU9tN25GRE1HeGNsZ1N6NU5pS25LRSJ9.V6Rj_Sjz9hlQjBrUU45ISmSclAzd9s3930W-G96DDLo'
bucket_key = "excellerateconfiguratorbucket"
object_name = "hangerassemblies.rvt"
file_path = 'C:\\Users\\mmendez\\Vision Projects\\Configurator\\excellerate-configurator-resources\\AssemblyConfigurationTestProject.rvt'
upload_response = upload_to_bucket(authorization, bucket_key, object_name, file_path)
print(upload_response.text)
