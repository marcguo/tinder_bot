'''
This file includes the definition of the User class.
The user class includes a Tinder user's unique ID, 
their name, and the distance between you and the user.
'''

class User:
    def __init__(self, id, name, distance):
        self.id = id
        self.name = name
        self.distance = distance
