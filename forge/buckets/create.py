import requests
import urllib.parse

def create_bucket(authorization, bucket_key, policy):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization, # ex: 'Bearer token_id'
    }
    data = {
        'bucketKey': bucket_key,
        'policyKey': policy
    }

    response = requests.post('https://developer.api.autodesk.com/oss/v2/buckets', headers=headers, json=data)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJjbGllbnRfaWQiOiJaYUcxcGRPN3lORHpiZ0dGQVVta2ZsRGVEbG9EYVJQNCIsImV4cCI6MTUzNzgwOTkyNywic2NvcGUiOlsiYnVja2V0OmNyZWF0ZSIsImRhdGE6cmVhZCIsInZpZXdhYmxlczpyZWFkIiwiYWNjb3VudDpyZWFkIl0sImF1ZCI6Imh0dHBzOi8vYXV0b2Rlc2suY29tL2F1ZC9qd3RleHA2MCIsImp0aSI6IlNkdVA3NnZLSG5DM04yOGEwMGRuTDU4cUdlZTBSOTZQeHlrVzh5c3lETHZBOUsxQmQ2V1prQ3Jlc0trUm8yaFYifQ.eL9O4jBQIivhb-Tm2T8RNTVXUSnfkUX0sXrD-pzYG4c'
bucket_key = 'excellerateconfiguratorbucket'
policy = 'persistent' #transient, temporary, persistent
create_bucket_response = create_bucket(authorization, bucket_key, policy)
print(create_bucket_response)
print(create_bucket_response.text)