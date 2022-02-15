import json
from random import seed
import random 
seed(1)
def random_latitude():
    value = random.random()
    value = (value*2) + 16
    return value
def random_longitude():
    value = random.random()
    value = (value*2) + 82
    return value

def random_composition():
    list = ["stony", "iron", "stony-iron"]
    value = random.choice(list)
    return value

data = {}

data['sites'] = []

for x in range (1,11): 
    data['sites'].append( {'site_id': x, 'latitude': random_latitude(), 'longitude' : random_longitude(), 'composition': random_composition() } )

with open('random_sites.json', 'w') as out:
    json.dump(data, out, indent=2)
