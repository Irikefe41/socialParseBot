import requests
import useJson


def geolocate(location):

	_creds = useJson.readJson('googleAPI.json')
	_url = "https://maps.googleapis.com/maps/api/geocode/json"

	params = {
	    'address': location,
	    # 'sensor': 'false',
	    # 'region': 'uk'
	    'key': _creds['googleAPI']
	}

	response = requests.get(_url, params)
	res = response.json()
	bound = res['results'][0]['geometry']['viewport']

	return [bound['northeast']['lng'], bound['northeast']['lat'], bound['southeast']['lng'], bound['southeast']['lat']]