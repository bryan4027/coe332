# This folder belongs to Bryan Acosta's homework 2.
Eid ba25389. TACC id: ba25389.

# Calculating Travel Times of Mars Rover using JSON files
The purpose of this project is to generate a listing of target sites for a Mars Rover's journey. This assignment helps practice newly learned python and JSON skills. JSON files are important because it is the most universal data type that can be read by muliple programming languages - making it ideal for big programs.

# Part 1 Python Script:
This python script's purpose is to create a JSON file that lists the random sites. It uses the random function to generate random numbers to assign numbers from 16-18 for the latitude and numbers from 82-84 for the longitude. It also creates a list of compositions and randomly chooses one from the list. It adds each site onto a list one by one, and then in the end it dumps that list into a JSON file.



# Part 2 Python Script:
This second Python Script reads in the JSON file and assigns it onto a local list. Then, the script reads in indivual data like latitude, longitude, and composition for each individual site. Then, it calculates the trip time between sites, adds up the totals, and prints the results for the entire trip.


# Instructions for Program: 
1. Run `generate_sites.py` to generate the JSON file
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
3. Run `calculate_trip.py` to read in the produced JSON file and calculate the trip times
4. Observe the results - it prints the leg, which is an indicator of how many sites the rover has visited, the time that it took to travel between each leg, how long the rover took to sample the site, the total number of legs for the overall trip and the total time for the entire trip.


