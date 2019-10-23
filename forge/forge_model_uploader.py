import requests
import json
import urllib
import base64
import time
import click

def verify_manifest(authorization, urn):
    headers = {
        'Authorization': authorization,
    }

    manifest_response = requests.get('https://developer.api.autodesk.com/modelderivative/v2/designdata/' + urn + '/manifest', headers=headers)
    print(manifest_response.text)
    return manifest_response

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
    response = requests.post('https://developer.api.autodesk.com/modelderivative/v2/designdata/job', data=json.dumps(data), headers=headers)
    print(response.text)
    return response.json()

def upload_to_bucket(authorization, bucket_key, object_name, file_path):
    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/octet-stream'
    }
    with open(file_path, 'rb') as files:
        base_endpoint = 'https://developer.api.autodesk.com/oss/v2/buckets/'
        bucket_object = '{0}/objects/{1}'.format(bucket_key, object_name)
        object_endpoint = urllib.parse.urljoin(base_endpoint, bucket_object)
        response = requests.put(object_endpoint, headers=headers, data=files)
    return response.json()

def retrieve_token(client_id, client_secret, grant_type, scope):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = [
        ('client_id', client_id),
        ('client_secret', client_secret),
        ('grant_type', grant_type),
        ('scope', scope),
    ]
    response = requests.post('https://developer.api.autodesk.com/authentication/v1/authenticate', headers=headers, data=data)
    return response.json()

def urn_to_base64(urn):
        return base64.b64encode(urn.encode()).rstrip(b'=').decode()

def translate_and_upload(file_path, object_name, project_name, client_id, client_secret, bucket_key):
    file_path = file_path + project_name
    policy = 'persistent' #transient, temporary, persistent
    grant_type = 'client_credentials'
    scope ='bucket:create bucket:read data:create data:write data:read viewables:read'
    to_type = 'svf'

    token = retrieve_token(client_id=client_id, client_secret=client_secret, grant_type=grant_type, scope=scope)
    access_token = 'Bearer ' +  token['access_token']
    print(access_token)

    print('Uploading to Bucket...')
    upload_response = upload_to_bucket(access_token, bucket_key, object_name, file_path)
    print('Bucket Upload Reponse {}'.format(str(upload_response)))

    '''
    Here we translate and the wait for the model
    to finish translating
    '''

    urn = upload_response['objectId']
    print(urn)
    urn_64 = urn_to_base64(urn)
    translate_reponse = translate_urn(access_token, urn_64, to_type)
    print(translate_reponse)

    completed = False
    while not completed:
        time.sleep(3)
        verify_response = verify_manifest(access_token, urn_64)
        response_json = verify_response.json()
        if response_json['status'] == 'success':
            completed = True
            print('Completed!')
            print(response_json['urn'])
        elif response_json['status'] == 'inprogress':
            print('still translating..')
            print(response_json['progress'])
        else:
            print(response_json)
            continue

def create_bucket(client_id, client_secret, bucket_key):
    grant_type = 'client_credentials'
    policy = 'persistent'
    scope ='bucket:create data:read viewables:read account:read data:create'
    token = retrieve_token(client_id, client_secret, grant_type, scope)
    authorization = 'Bearer ' +  token['access_token']

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

@click.command()
@click.option('-j', '--jsonfile', help="json file with required object")
@click.option('-b', '--with-bucket', is_flag=True, help="create forge bucket for objects")
def cli_entry_point(jsonfile, with_bucket):
    with open(jsonfile) as f:
        data = json.load(f)
        client_id = data['client_id']
        client_secret = data['client_secret']
        object_name = data['object_name']
        project_name = data['project_name']
        file_path = data['file_path']
        bucket_key = data['bucket_key']

    if with_bucket:
        buckets = ['','','']
        with click.progressbar(buckets) as bar:
            click.echo('Creating Bucket: {}'.format(bucket_key))
            create_bucket(client_id, client_secret, bucket_key)
            for bucket in bar:
                time.sleep(1)
    models = ['']
    with click.progressbar(models) as bar:
        click.echo('Translating: {}'.format(project_name))
        translate_and_upload(file_path, object_name, project_name, client_id, client_secret, bucket_key)
        for model in bar:
            time.sleep(1)

if __name__ == '__main__':
    cli_entry_point()