import pytest
import json
from analyze_water import calculate_turbidity
from analyze_water import calculate_minimum_time
from analyze_water import main

def test_calculate_turbidity():
    with open('datatest.json', 'r') as f:
        testdata = json.load(f)
    with open('datatest2.json', 'r') as f:
        testdata2 = json.load(f)
        

    assert(calculate_turbidity(testdata['turbidity_data']) == 1.1992)
    assert isinstance(calculate_turbidity(testdata['turbidity_data']), float) == True
    assert isinstance(calculate_turbidity(testdata['turbidity_data']), str) != True
    assert(calculate_turbidity(testdata2['turbidity_data']) == 1.4632)
    assert(calculate_turbidity(testdata2['turbidity_data']) != 1.8482)

1.4632    
    #assert isinstance(calculate_turbidity([{'a': 1}, {'a': 2}], 'a'), float)
    #assert isinstance(calculate_turbidity([{'a': 1}, {'a': 2}], 'a'), float)

def test_calculate_minimum_time():

    assert(calculate_minimum_time(1.1992) == 8.991600232149228)
    assert(calculate_minimum_time(1.3422) == 14.567852422768159)
    assert(calculate_minimum_time(1.4244) == 17.510062728806584)
    assert isinstance(calculate_minimum_time(1.4244), float) == True
    assert isinstance(calculate_minimum_time(1.4244), str) == False

def pytest():

    test_calculate_turbidity()
    test_calculate_minimum_time()


if __name__ == '__pytest__':
    pytest()
