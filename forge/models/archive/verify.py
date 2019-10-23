import requests

def verify_manifest(authorization, urn):
    headers = {
        'Authorization': authorization,
    }

    manifest_response = requests.get('https://developer.api.autodesk.com/modelderivative/v2/designdata/' + urn + '/manifest', headers=headers)
    return manifest_response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJaYUcxcGRPN3lORHpiZ0dGQVVta2ZsRGVEbG9EYVJQNCIsImV4cCI6MTUzNzgxMDI1MCwic2NvcGUiOlsiYnVja2V0OmNyZWF0ZSIsImRhdGE6cmVhZCIsInZpZXdhYmxlczpyZWFkIiwiYWNjb3VudDpyZWFkIiwiZGF0YTpjcmVhdGUiXSwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoiMXkwWE5Sb29sZVNmU3g3VXY3NnZHNU9ueUJLUXhqQUU4akdRQ0pBN3M1bU9tN25GRE1HeGNsZ1N6NU5pS25LRSJ9.V6Rj_Sjz9hlQjBrUU45ISmSclAzd9s3930W-G96DDLo'
urn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZXhjZWxsZXJhdGVjb25maWd1cmF0b3JidWNrZXQvaGFuZ2VyYXNzZW1ibGllcy5ydnQ'
#     'dXJuOmFkc2sud2lwcHJvZDpmcy5maWxlOnZmLkduRXlaMEhIUnFLWnpodk5fOFVrclE/dmVyc2lvbj0xX2FuY2hvcg'
response = verify_manifest(authorization, urn)
print(response.text)