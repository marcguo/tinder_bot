'''
API's are based on https://github.com/fbessez/Tinder.
'''

# To perform RESTful API requests.
import requests
# To assemble and parse JSON objects.
import json
from user import *
import config
from location import *
from log import *

# Common headers used for all API requests.
HEADERS = {'x-auth-token': config.X_AUTH_TOKEN , 
            'user-agent': 'Tinder/11.4.0 (iPhone; iOS 12.4.1; Scale/2.00)', 
            'content-type': 'application/json'}

def get_rec_list():
    '''
    Gets a list of recommended users to interact with.
    
    @rtype  list
    @return A list of User objects that contains all users from the /user/recs API GET
            request.
    '''

    url = 'https://api.gotinder.com/user/recs'
    
    raw_response = requests.get(url, headers = HEADERS)
    
    response = raw_response.json()
    
    try:
        if 401 == response['status']:
            print('401 (Unauthorised) returned from the API call.')
            log('401 (Unauthorised) returned from the API call.')
            exit()
    except:
        print(response)
        log(response)
        exit()
    
    try:    
        # This is a list that contains all rec'd users.
        results = response['results']
    except:
        print('Could not get rec list.')
        log('Could not get rec list.')
        print(response)
        log(response)
        
        return []
    
    rec_user_list = []
    
    for result in results:
        id = result['_id']
        name = result['name']
        distance = result['distance_mi']
        rec_user = User(id, name, distance)
        rec_user_list.append(rec_user)
        
    return rec_user_list
    
def get_match_list(count):
    '''
    Gets a list of matched users to interact with.
    
    NOTE: This is still in progress.
    
    @type  count: integer
    @param count: Count of matches to get at a time.
    '''

    url = 'https://api.gotinder.com/v2/matches?count={}'.format(str(count))
    
    raw_response = requests.get(url, headers = HEADERS)
    
    response = raw_response.json()
    
    matches = response['data']['matches']
    
    match_list = []
    
    for match in matches:
        for key in match:
            print(key)
            
        return
        
        match_detail = match['person']
        id = match_detail['_id']
        name = match_detail['name']
        distance = match_detail['distance_mi']
        matched_user = User(id, name, distance)
        match_list.append(matched_user)
        
    return match_list
    
def get_user(id):
    '''
    Gets a specific user's profile.
    
    @type  id: string
    @param id: User ID.
    '''

    url = 'https://api.gotinder.com/user/{}'.format(id)
    
    raw_response = requests.get(url, headers = HEADERS)
    
    response = raw_response.json()
    
    print(response)
    
def like_user(id):
    '''
    Likes a specific user.
    
    @type  id: string
    @param id: User ID.
    '''
    
    url = 'https://api.gotinder.com/like/{}'.format(id)
    
    raw_response = requests.get(url, headers = HEADERS)
    
    response = raw_response.json()
    
def change_location(lat, lon):
    '''
    Changes my location to a specified location.
    
    @type  lat: string
    @param lat: Latitude value.
    
    @type  lon: string
    @param lon: Longitude value.
    '''
    
    url = 'https://api.gotinder.com/user/ping'
    data = {'lat': lat, 'lon': lon}
    
    raw_response = requests.post(url, headers = HEADERS, data = json.dumps(data), verify = True)
    response = raw_response.json()
    
def travel(lat, lon):
    '''
    Travels/Sets the current location to a specified location.
    
    @type  lat: string
    @param lat: Latitude value.
    
    @type  lon: string
    @param lon: Longitude value.
    '''
    
    url = 'https://api.gotinder.com/passport/user/travel'
    data = {'lat': lat, 'lon': lon}
    
    raw_response = requests.post(url, headers = HEADERS, data = json.dumps(data), verify = True)
    response = raw_response.json()
    
def message(id, message):
    '''
    Sends a message to a user.
    
    @type  id: string
    @param id: User ID.
    
    @type  message: string
    @param message: Longitude value.
    '''
    
    url = 'https://api.gotinder.com/user/matches/{}'.format(id)
    data = {"message": message}
    
    raw_response = requests.post(url, headers = HEADERS, data = json.dumps(data), verify = False)
    response = raw_response.json()
    
    print(response)
    
def get_geocode(address):
    '''
    Gets the latitude and longitude of an address.
    
    @type  address: string
    @param address: Address of the city/place to query the geocoding of.
    
    @rtype  Location
    @return A Location object containing the location info (latitude, longitude...).
    '''
    
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address, config.GOOGLE_API_KEY)

    raw_response = requests.get(url)
    
    response = raw_response.json()
    
    try:
        result = response['results'][0]
    except:
        print('The address given is invalid.')
        return False
    
    geometry = result['geometry']
    
    location = geometry['location']
    
    lat = location['lat']
    
    lon = location['lng']
    
    return Location(str(lat), str(lon))
    