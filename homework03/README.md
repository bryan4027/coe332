# This folder belongs to Bryan Acosta's homework 3.
Eid ba25389. TACC id: ba25389.

# Analyzing Mar's Rover's Collected Data
The purpose of this project is to read in a JSON file of the collected data, analyze it, and determine if the water is safe for sample testing. It determines this based off the 5 most recent data points. This project enhances my skills with JSON manipulation, huge list manipulation, Python organization, documentation, logging, unit testing, and more.

# Part 1 Python Script:
This python script's purpose is to read in a JSON file and calculate the average turbidity of the 5 most recent data points. It decided whether the water is safe or not for testing the samples. Then, it uses that value to calculate the minimum amount of hours neccesary for the water to be safe.

<details>
<summary>Show python script 1: analyze_water.py</summary>

Python

```python:
import json
import math
import logging
logging.basicConfig(level=logging.DEBUG)
def calculate_turbidity(datavec: list) -> float:
    '''
    This function:
         This function reads in a list of data points recorded real time, takes the last 5 data points and calculates the average Turbidity and returns it
    Args:
         datavec (list): The input is a list of dictionaries with the following values: datetime - a date in the format of a string, sample_volume - a double, calibration_constant - a double, detector_current - a double,  analyzed_by - a string
    Returns:
         this function returns the average turbidity of the last five data points recorded
    '''
    x = -5
    global lastfivedicts
    lastfivedicts = []
    
    for i in range(0,5):
            lastfivedicts.append(datavec[x])
            x = x+1
    avgturb = 0
    for i in range(0,len(lastfivedicts)):
        calibration_const = float(lastfivedicts[i]['calibration_constant'])
        current = float(lastfivedicts[i]['detector_current'])
        avgturb = avgturb + (calibration_const*current)
    avgturb = avgturb/(len(lastfivedicts))
    return avgturb
    

def calculate_minimum_time(avgturb: float) -> float:
'''
    This function:
         This function reads in the average turbidity of the 5 most recent data points, uses the given equation to calculate the minimum amount of time required, and returns it
    Args:
         avgturb is the average turbidity of the 5 most recent data points. it is always a float.
    Returns:
         this function returns the the amount of time that it takes for the turbidity to get to a safe value. 
'''
    global hour
    hour = 0
    hour  = math.log((1/avgturb),0.98)
    return (hour)

def printstuff(avgturb: float, time: float) ->None:
    print("\n     Avg Turbidity: ",avgturb)
    if (avgturb >= 1):
        logging.warning('Warning: Turbidity is above threshold for safe use ')
        print ("     Minimum time required to return below a safe threshold = ",hour, "\n")
    if (avgturb < 1):
        logging.info ('Turbidity is safe for use. \n' )
    
    
def main():

    with open('turbidity_data.json', 'r') as f:
        datavec = json.load(f)

    turb  = calculate_turbidity(datavec['turbidity_data'])
    time = calculate_minimum_time(turb)
    printstuff(turb, time)


if __name__ == '__main__':
    main()
```
</details>

# Part 2 Python Script:
This second Python Script is used to test the correctness of the `analyze_water.py` file. It uses unit testing to individually test if the functions input and output are correct, if the variables are correct types and amounts, and more using Pytest.

<details>
<summary>Show python script 2: test_analyze_water.py </summary>
Python

```python:

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
```
</details>

# Instructions for Program: 
1. Download `turbidity_data.json` by running the following into the terminal:
```python:
wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```
2. Observe the produced JSON file `turbidity_data.json` to ensure that the file was produced correctly. It should look like the following:
```python:
{
  "turbidity_data": [
    {
      "datetime": "2022-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.022,
      "detector_current": 1.137,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 0.975,
      "detector_current": 1.141,
      "analyzed_by": "C. Milligan"
    },
```
3.  Run `analyze_water.py` to read in the JSON file and analyze it. enter the following into the command line: 
```python: 
python3 analyze_water.py
``` 
4. Observe Output. When the water is safe the output will look like this:
    
and when the water is not safe, the output will look like this:
```python:
         Avg Turbidity:  1.1444604
WARNING:root:Warning: Turbidity is above threshold for safe use
     Minimum time required to return below a safe threshold =  6.678969181162484

3. Run `calculate_trip.py` to read in the produced JSON file and calculate the trip times. enter the following into the command line:
```python:
python3 calculate_trip.py
```

4. Observe the results - it prints the leg, which is an indicator of how many sites the rover has visited, the time that it took to travel between each leg, how long the rover took to sample the site, the total number of legs for the overall trip and the total time for the entire trip.

```python:
leg =  0 , time to travel =  10.028412380420631 , time to sample =  1  hr
leg =  1 , time to travel =  4.167982942347527 , time to sample =  2  hr
leg =  2 , time to travel =  1.4068974074119245 , time to sample =  1  hr
leg =  3 , time to travel =  4.197843984486427 , time to sample =  2  hr
leg =  4 , time to travel =  8.69800562663968 , time to sample =  1  hr
leg =  5 , time to travel =  5.879956699140427 , time to sample =  1  hr
leg =  6 , time to travel =  1.9485545577433083 , time to sample =  2  hr
leg =  7 , time to travel =  1.2846683925065174 , time to sample =  3  hr
leg =  8 , time to travel =  10.12537765815768 , time to sample =  3  hr
leg =  9 , time to travel =  5.4395822045370705 , time to sample =  1  hr

 total legs =  10 , totaltime =  70.17728185339121
```
