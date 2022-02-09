import json
import math
def compute_distances(input_sites):
    originalx = 82
    originaly = 16
    totallegs = 0
    totaltime = 0
    for x in range(len(input_sites)):
        targetx = float(input_sites[x]['longitude']) 
        targety = float(input_sites[x]['latitude'])
        targetcomp = str(input_sites[x]['composition'])

        triptime = calc_gcd(targetx, targety, originalx, originaly)
        triptime = triptime/10
        originalx = targetx
        originaly = targety
        totallegs = totallegs +1
        totaltime = totaltime + triptime + calc_sample_time(targetcomp)
        print('leg = ' ,x, ', time to travel = ', triptime, ', time to sample = ' , calc_sample_time(targetcomp), ' hr')
    print('\n total legs = ', totallegs, ', totaltime = ' , totaltime)
        
import math

mars_radius = 3389.5    # km

def calc_sample_time(compname):
    if compname == 'stony':
        return 1
    if compname == 'iron':
        return 2
    if compname == 'stony-iron':
        return 3


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )


        
with open('random_sites.json', 'r') as f:
    ml_data = json.load(f)

compute_distances(ml_data['sites'])
