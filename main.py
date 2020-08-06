'''
This is the main script to be run. 
Right now it only supports liking all available users at the current 
location set.
'''

from api import *
import time
import config
import sys
from log import *
import datetime

CITY = 'Toronto'
LOCATION = Location('', '')
UNLIMITED_LIKES = False

def auto_like():
    '''
    Automatically keeps liking all available users.
    '''
    
    like_count = 0

    while UNLIMITED_LIKES or like_count < config.LIKE_GOAL:
        rec_user_list = get_rec_list()
    
        for user in rec_user_list:
            try:
                # Set the current location.
                set_location(LOCATION)
                like_user(user.id)
                like_count += 1
            
                try:
                    print(u'Liked {}, distance {}'.format(user.name, user.distance))
                    log(u'Liked {}, distance {}'.format(user.name, user.distance))
                except:
                    print("Could not print the current user's name. It's probably because of the encoding?")
                    log("Could not print the current user's name. It's probably because of the encoding?")
            except:
                try:
                    print('Could not like {}'.format(user.name))
                    log('Could not like {}'.format(user.name))
                except:
                    print('Could not like the current user.')
                    log('Could not like the current user.')
    
            time.sleep(1)

def set_location(location):
    '''
    Sets the current location to a specified location.
    
    @type  lat: string
    @param lat: Latitude value.
    
    @type  lon: string
    @param lon: Longitude value.
    '''
    
    lat = location.lat
    lon = location.lon
    
    travel(lat, lon)
    change_location(lat, lon)
    
    
# Remove the existing log.
remove()
    
# Log the starting time.
log(str(datetime.datetime.now()))

# Get the location to set from the command line argument.
CITY = sys.argv[1]

# Set the global location variable to the city that we want to travel to.
LOCATION = get_geocode(CITY)
if not LOCATION:
    exit()
    
print(LOCATION.lat + ' ' + LOCATION.lon)
log(LOCATION.lat + ' ' + LOCATION.lon)
# Automatically like all available users.
auto_like()

log(str(datetime.datetime.now()))
log('Finished executing.')

# TODO: Like/Match ratio data analyses of different locations in the world.

# TODO: Make it multithreaded. One thread for liking users and another for chatting.

# TODO: Make it automatically switch locations based on time and cities' popularity.
