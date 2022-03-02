#!/usr/bin/env python3
import json
from typing import List
import logging
import socket
import sys

format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)

def making_summary(ml_data):
    
    print('\nSummary data following meteorite analysis:')
    
    print('\nAverage mass of 30 meteor(s):',compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'), '\n')

    tracker = [0,0,0,0]
    for row in ml_data['meteorite_landings']:
        if check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Northern & Western': 
             tracker[0] +=1
        if check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Northern & Eastern':
             tracker[1] +=1
        if check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Southern & Western':
             tracker[2] +=1
        if check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Southern & Eastern':
             tracker[3] +=1
    print('Hemisphere summary data:')
    print('There were',tracker[0] ,' meteors found in the  Northern & Western Quadrant.')
    print('There were',tracker[1] ,' meteors found in the  Northern & Eastern Quadrant.')
    print('There were',tracker[2] ,' meteors found in the  Southern & Western Quadrant.')
    print('There were',tracker[3] ,' meteors found in the  Eastern & Western Quadrant.')
    
    print('\nClass summary data:')

    dictofclasses= (count_classes(ml_data['meteorite_landings'], 'recclass'))
    for key, value in dictofclasses.items():
        print('The  ', key, ' class was found ', value, 'times.')



def compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).

    Returns:
        result (float): Average value.
    """
    if (len(a_list_of_dicts) == 0):
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return(total_mass / len(a_list_of_dicts) )


def check_hemisphere(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.

    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.

    Returns:
        location (string): Short string listing two hemispheres.
    """
    if latitude == 0 or longitude == 0:
        #logging.error('youre not really in a hemisphere')
        raise(ValueError)
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    return(location)


def count_classes(a_list_of_dicts: List[dict], a_key_string: str) -> dict:
    """
    Iterates through a list of dictionaries, and pulls out the value associated
    with a given key. Counts the number of times each value occurs in the list of
    dictionaries and returns the result.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value.

    Returns:
        classes_observed (dict): Dictionary of class counts.

    """
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)


def main():
    input = str(sys.argv[1])

    logging.debug('entering main loop')

    with open(input, 'r') as f:
        ml_data = json.load(f)

    logging.debug(f'the type of ml_data is {type(ml_data)}')
    making_summary(ml_data)
    #print(count_classes(ml_data['meteorite_landings'], 'recclass'))


if __name__ == '__main__':
    main()


