from app.forge.api import api
from app import app

app_config = app.config

def refresh_token():
    client_id = app_config['FORGE_CLIENT']
    client_secret = app_config['FORGE_SECRET']
    grant_type = 'client_credentials'
    scope = 'data:read viewables:read'
    api_instance = api(client_id=client_id,
                       client_secret=client_secret,
                       grant_type=grant_type,
                       scope=scope)
    refreshed_token = api_instance.retrieve_token_2leg()

    try:
        access_token = refreshed_token["access_token"]
        return access_token
    except:
        return None