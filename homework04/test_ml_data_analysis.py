import pytest
import json
from ml_data_analysis import *

def test_count_classes():
    with open('Meteorite_Landings.json', 'r') as f:
        ml_data = json.load(f)
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), dict) == True
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), int) == False
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), int) != True
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), dict) != False
    assert isinstance(count_classes(ml_data['meteorite_landings'], 'recclass'), str) == False 


def test_compute_average_mass():
    with open('Meteorite_Landings.json', 'r') as f:
        ml_data = json.load(f)
    assert(compute_average_mass(ml_data['meteorite_landings'],'mass (g)') > 0)
    assert(compute_average_mass(ml_data['meteorite_landings'],'mass (g)') != 0)
    assert isinstance(compute_average_mass(ml_data['meteorite_landings'],'mass (g)'), float) == True
    assert isinstance(compute_average_mass(ml_data['meteorite_landings'],'mass (g)'), list) != True
    assert isinstance(compute_average_mass(ml_data['meteorite_landings'],'mass (g)'), list) == False

def test_check_hemisphere():
    assert isinstance(check_hemisphere(1,1), str) == True
    assert isinstance(check_hemisphere(1,1), float) == False
    assert ((check_hemisphere(1,1)) == 'Northern & Eastern')
    assert ((check_hemisphere(-1,1)) == 'Southern & Eastern')
    assert ((check_hemisphere(1,-1)) == 'Northern & Western')



def pytest():
    test_count_classes()
    test_compute_average_mass()
    test_check_hemisphere()
    

if __name__ == '__pytest__':
    pytest()
