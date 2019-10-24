import requests
from config import useJson

_creds = useJson.readJson('googleAPI.json')

_url = "https://maps.googleapis.com/maps/api/geocode/json"

params = {
    'address': 'Lagos',
    # 'sensor': 'false',
    # 'region': 'uk'
    'key': _creds['googleAPI']
}
response = requests.get(_url, params)
res = response.json()
print(res['results'][0]['geometry']['viewport'])
# print(res['viewport'])