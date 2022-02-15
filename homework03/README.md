# This folder belongs to Bryan Acosta's homework 2.
Eid ba25389. TACC id: ba25389.

# Calculating Travel Times of Mars Rover using JSON files
The purpose of this project is to generate a listing of target sites for a Mars Rover's journey. This assignment helps practice newly learned python and JSON skills. JSON files are important because it is the most universal data type that can be read by muliple programming languages - making it ideal for big programs.

# Part 1 Python Script:
This python script's purpose is to create a JSON file that lists the random sites. It uses the random function to generate random numbers to assign numbers from 16-18 for the latitude and numbers from 82-84 for the longitude. It also creates a list of compositions and randomly chooses one from the list. It adds each site onto a list one by one, and then in the end it dumps that list into a JSON file.

<details>
<summary>Show python script 1: generate_sites.py</summary>

Python

```python:
import json
from random import seed

for x in range (1,11): 
    data['sites'].append( {'site_id': x, 'latitude': random_latitude(), 'longitude' : random_longitude(), 'composition': random_composition() } )

with open('random_sites.json', 'w') as out:
    json.dump(data, out, indent=2)
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
1. Run `generate_sites.py` to generate the JSON file. enter the following into the command line: 
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
