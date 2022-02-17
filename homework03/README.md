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
This second Python Script reads in the JSON file and assigns it onto a local list. Then, the script reads in indivual data like latitude, longitude, and composition for each individual site. Then, it calculates the trip time between sites, adds up the totals, and prints the results for the entire trip.

<details>
<summary>Show python script 2: calculate_trip.py </summary>
Python

```python:

import json
        
with open('random_sites.json', 'r') as f:
    ml_data = json.load(f)

compute_distances(ml_data['sites'])
```
</details>

# Instructions for Program: 
1. Download `turbidity_data.json` by running the following into the terminal:
```python:
wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```
2.  Run `analyze_water.py` to generate the JSON file. enter the following into the command line: 
```python: 
python3 generate_sites.py
``` 
2. Observe the produced JSON file `random_sites.json` to ensure that the file was produced correctly. It should look like the following:
```python:
{
  "sites": [
    {
      "site_id": 1,
      "latitude": 16.268728488224802,
      "longitude": 83.69486747387447,
      "composition": "stony"
    },
    {
      "site_id": 2,
      "latitude": 16.510138051478844,
      "longitude": 82.99087017418388,
      "composition": "iron"
    },
```
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
