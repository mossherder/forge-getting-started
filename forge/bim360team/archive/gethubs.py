
def get_hubs(authorization):
    import requests

    headers = {
        'Authorization': authorization,
    }

    response = requests.get('https://developer.api.autodesk.com/project/v1/hubs', headers=headers)
    return response

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6Imp3dF9zeW1tZXRyaWNfa2V5In0.eyJ1c2VyaWQiOiJEVTNOUlZITEc0TkoiLCJleHAiOjE1MzA2NDkxMTgsInNjb3BlIjpbImRhdGE6Y3JlYXRlIiwiZGF0YTp3cml0ZSIsImRhdGE6cmVhZCIsImJ1Y2tldDpyZWFkIiwiYnVja2V0OnVwZGF0ZSIsImJ1Y2tldDpjcmVhdGUiXSwiY2xpZW50X2lkIjoiQUxZSjZYNWpoTkw3WTZDTVBsa2g1UVhqS0ZGcFlRSFoiLCJncmFudF9pZCI6Im5rWjBRalNOS1JIaTFhZlMycWZJYmZPanJOaHEyeldiIiwiYXVkIjoiaHR0cHM6Ly9hdXRvZGVzay5jb20vYXVkL2p3dGV4cDYwIiwianRpIjoibmowQ2phd1lETDM0OE9qR1p3V09VU1d0MmpGMkZDYTBuQ0JOZkNxcXJ1bjUwb1RNR2hleFlLTm8yajE1dVA3byJ9.m25axEwKF4vqxDbBXy7mrqoxajTjR7pO21jUtFFFf1U'
get_hubs_response = get_hubs(authorization)
print(get_hubs_response.text)