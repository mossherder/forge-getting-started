import requests
import json

def translate_urn(authorization, urn, to_type):
    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json',
    }
    data = {
        "input": {
            "urn": urn,
        },
        "output": {
            "destination": {
                "region": "us"
            },
            "formats": [
                {
                    "type": to_type,
                    "views": [
                        "3d"
                    ]
                },
            ]
        }
    }
    response = requests.post('https://developer.api.autodesk.com/modelderivative/v2/designdata/job' , data=json.dumps(data), headers=headers)
    return response


authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJaYUcxcGRPN3lORHpiZ0dGQVVta2ZsRGVEbG9EYVJQNCIsImV4cCI6MTUzNzgxMDI1MCwic2NvcGUiOlsiYnVja2V0OmNyZWF0ZSIsImRhdGE6cmVhZCIsInZpZXdhYmxlczpyZWFkIiwiYWNjb3VudDpyZWFkIiwiZGF0YTpjcmVhdGUiXSwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoiMXkwWE5Sb29sZVNmU3g3VXY3NnZHNU9ueUJLUXhqQUU4akdRQ0pBN3M1bU9tN25GRE1HeGNsZ1N6NU5pS25LRSJ9.V6Rj_Sjz9hlQjBrUU45ISmSclAzd9s3930W-G96DDLo'
urn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZXhjZWxsZXJhdGVjb25maWd1cmF0b3JidWNrZXQvaGFuZ2VyYXNzZW1ibGllcy5ydnQ'
to_type = "svf"
translation_response = translate_urn(authorization, urn, to_type)
print(translation_response.text)