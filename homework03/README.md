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
```python:
     Avg Turbidity:  0.86
INFO:root:Turbidity is safe for use.
```
and when the water is not safe, the output will look like this:
```python:
 Avg Turbidity:  1.1444604
WARNING:root:Warning: Turbidity is above threshold for safe use
     Minimum time required to return below a safe threshold =  6.678969181162484
```
    
5. In order to run the next script, you will need to ensure that you have these next two JSON files within the directory. They are filled with DATA where it is easy to calculate the results and thus figure out if the function is working correctly. If you do not have either of them in the directory, please creat files named `datatest.json`and `datatest2.json`. Then copy paste the content accordingly.
    
a. First JSON file   
<details>
<summary>Show python script 1: generate_sites.py</summary>
    
JSON
```python:
{
  "turbidity_data": [
    {
      "datetime": "2022-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 02:00",
      "sample_volume": 1.15,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 03:00",
      "sample_volume": 1.18,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "R. Zhang"
    },
    {
      "datetime": "2022-02-01 04:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "J. Maertz"
    },
    {
      "datetime": "2022-02-01 05:00",
      "sample_volume": 1.17,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "K. Judkins"
    },
    {
      "datetime": "2022-02-01 06:00",
      "sample_volume": 1.24,
      "calibration_constant": 1.0,
      "detector_current": 1.1992,
      "analyzed_by": "F. Zhou"
    } ] }    
```
</details>
    
b. and the second JSON file:
    
<details>
<summary>Show python script 1: generate_sites.py</summary>
    
JSON
```python:
{
  "turbidity_data": [
    {
      "datetime": "2022-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 02:00",
      "sample_volume": 1.15,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2022-02-01 03:00",
      "sample_volume": 1.18,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "R. Zhang"
    },
    {
      "datetime": "2022-02-01 04:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "J. Maertz"
    },
    {
      "datetime": "2022-02-01 05:00",
      "sample_volume": 1.17,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "K. Judkins"
    },
    {
      "datetime": "2022-02-01 06:00",
      "sample_volume": 1.24,
      "calibration_constant": 1.0,
      "detector_current": 1.4632,
      "analyzed_by": "F. Zhou"
    } ] }  
```
</details>
    
6. Run `test_analyze_water.py` to test the `analyze_water.py` correctness. enter the following into the command line:
```python:
python3 test_analyze_water.py
```

7. Observe the results - if it runs and does not display anything, then the code is correct. Otherwise, there is an error somewhere in your code, whether in function, inputs, variables, or more, depending on the output text.
