import requests
import twitter as twit
from ..utils import useJson


_creds = useJson.readJson('config.json')

def geolocate(location):

	_url = "https://maps.googleapis.com/maps/api/geocode/json"

	params = {
	    'address': location,
	    # 'region': 'uk'
	    'key': _creds['googleAPI']
	}

	response = requests.get(_url, params)
	res = response.json()
	bound = res['results'][0]['geometry']['viewport']
	print(bound)

	return  [str(bound['southwest']['lng']), str(bound['southwest']['lat']), 
				str(bound['northeast']['lng']), str(bound['northeast']['lat'])]

def grabTwitterPosts(zone='switzerland'):

	api = twit.Api(consumer_key=_creds['twitter']['consumer_key'],
                  consumer_secret=_creds['twitter']['consumer_secret'],
                  access_token_key=_creds['twitter']['access_token'],
                  access_token_secret=_creds['twitter']['access_token_secret'])

	print(api.VerifyCredentials())
	location = geolocate(zone)

	for line in api.GetStreamFilter(locations=location):
		print("@{} from {}.".format(line['user']['screen_name'], line['place']['country']))
		print("Tweeted: {}".format(line['text']))
		print('\n')

def grabFacebookPosts():
	pass

def grabRedditPosts():
	pass




