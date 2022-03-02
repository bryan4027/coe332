# This folder belongs to Bryan Acosta's homework 4.
Eid ba25389. TACC id: ba25389.






# Analyzing Meteorite Landings, Mass, and Composition using Docker
The purpose of this project is to create a script that reads in a JSON file listing Meteorite Landings and analyzes its mass, composition, numbers, and location. We then use `PYTEST`to run a test file that ensures the first script is working correctly. We then use a Dockerfile to create a Docker Container which serves as a developer enviornment ready for anybody to successfully run my program. This README gives explanations on everything we use as well as instructions to successfully run this program.

# ml_data_analysis.py
This python script's purpose is to read in a JSON file and use several functions to 

1. Compute the average mass
2. check in which quadrant of the planet the meteroite landed in
3. It counts how many metoeorites land of each different composition
4. Output the results of the previous 4 steps.

It outputs all this data into a nicely formatted output as follows:

```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 83857.3

Hemisphere summary data:
There were 6  meteors found in the  Northern & Western Quadrant.
There were 21  meteors found in the  Northern & Eastern Quadrant.
There were 3  meteors found in the  Southern & Western Quadrant.
There were 0  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   L5  class was found  1 times.
The   H6  class was found  1 times.
... etc!

```

<details>
<summary>Show python script 2: ml_data_analysis.py </summary>
Python

```python:
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
```
</details>

# test_ml_data_analysis.py
This second Python Script is used to test the correctness of the ml_data_analysis.py file. It uses unit testing to individually test if the functions input and output are correct, if the variables are correct types and amounts, and more using Pytest.
<details>
<summary>Show python script test_ml_data_analysis.py </summary>
Python

```python:
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
```
</details>

# Meteorite_Landings.json
This file is the input data. The input data should be in JSON format. JSON is is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.
    
A JSON formatted file is essentially a list of dictionaries. It is formatted like the following: 

```python
   {
  "dictionary name": [
    {
      "key": "value",
      "key2": "value",
      "key3": "value",
    },
    {
      "key": "value",
      "key2": "value",
      "key3": "value",
    }, 
    ... etc
    
```
<details>
<summary>Show Meteorite_Landings.json </summary>


```python:
{
  "meteorite_landings": [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },
    {
      "name": "Beeler",
      "id": "10002",
      "recclass": "H6",
      "mass (g)": "720",
      "reclat": "56.18333",
      "reclong": "10.23333",
      "GeoLocation": "(56.18333, 10.23333)"
    },
    {
      "name": "Brock",
      "id": "10003",
      "recclass": "EH4",
      "mass (g)": "107000",
      "reclat": "54.21667",
      "reclong": "-113",
      "GeoLocation": "(54.21667, -113.0)"
    },
    {
      "name": "Hillebrand",
      "id": "10004",
      "recclass": "Acapulcoite",
      "mass (g)": "1914",
      "reclat": "16.88333",
      "reclong": "-99.9",
      "GeoLocation": "(16.88333, -99.9)"
    },
    {
      "name": "Mitchell",
      "id": "10005",
      "recclass": "L6",
      "mass (g)": "780",
      "reclat": "-33.16667",
      "reclong": "-64.95",
      "GeoLocation": "(-33.16667, -64.95)"
    },
    {
      "name": "Ortiz",
      "id": "10006",
      "recclass": "EH4",
      "mass (g)": "4239",
      "reclat": "32.1",
      "reclong": "71.8",
      "GeoLocation": "(32.1, 71.8)"
    },
    {
      "name": "Souza",
      "id": "10007",
      "recclass": "LL3-6",
      "mass (g)": "910",
      "reclat": "44.83333",
      "reclong": "95.16667",
      "GeoLocation": "(44.83333, 95.16667)"
    },
    {
      "name": "Toler",
      "id": "10008",
      "recclass": "H5",
      "mass (g)": "30000",
      "reclat": "44.21667",
      "reclong": "0.61667",
      "GeoLocation": "(44.21667, 0.61667)"
    },
    {
      "name": "Hachey",
      "id": "10009",
      "recclass": "L6",
      "mass (g)": "1620",
      "reclat": "-31.6",
      "reclong": "-65.23333",
      "GeoLocation": "(-31.6, -65.23333)"
    },
    {
      "name": "Alexander",
      "id": "10010",
      "recclass": "L",
      "mass (g)": "1440",
      "reclat": "-30.86667",
      "reclong": "-64.55",
      "GeoLocation": "(-30.86667, -64.55)"
    },
    {
      "name": "Nunez",
      "id": "10011",
      "recclass": "Diogenite-pm",
      "mass (g)": "1000",
      "reclat": "16.39806",
      "reclong": "-9.57028",
      "GeoLocation": "(16.39806, -9.57028)"
    },
    {
      "name": "Chester",
      "id": "10012",
      "recclass": "L6",
      "mass (g)": "24000",
      "reclat": "19.08333",
      "reclong": "8.38333",
      "GeoLocation": "(19.08333, 8.38333)"
    },
    {
      "name": "Obermeyer",
      "id": "10013",
      "recclass": "Stone-uncl",
      "mass (g)": "2700",
      "reclat": "26.58333",
      "reclong": "85.56667",
      "GeoLocation": "(26.58333, 85.56667)"
    },
    {
      "name": "Paris",
      "id": "10014",
      "recclass": "L6",
      "mass (g)": "779",
      "reclat": "29.51667",
      "reclong": "35.05",
      "GeoLocation": "(29.51667, 35.05)"
    },
    {
      "name": "Kelly",
      "id": "10015",
      "recclass": "H4",
      "mass (g)": "1800",
      "reclat": "29.71667",
      "reclong": "77.95",
      "GeoLocation": "(29.71667, 77.95)"
    },
    {
      "name": "Smith",
      "id": "10016",
      "recclass": "H",
      "mass (g)": "3000",
      "reclat": "8.91667",
      "reclong": "8.43333",
      "GeoLocation": "(8.91667, 8.43333)"
    },
    {
      "name": "Wills",
      "id": "10017",
      "recclass": "Iron-IVA",
      "mass (g)": "50000",
      "reclat": "39.91667",
      "reclong": "42.81667",
      "GeoLocation": "(39.91667, 42.81667)"
    },
    {
      "name": "Becker",
      "id": "10018",
      "recclass": "CR2-an",
      "mass (g)": "160",
      "reclat": "24.41667",
      "reclong": "39.51667",
      "GeoLocation": "(24.41667, 39.51667)"
    },
    {
      "name": "Ray",
      "id": "10019",
      "recclass": "LL5",
      "mass (g)": "700",
      "reclat": "13.66033",
      "reclong": "28.96",
      "GeoLocation": "(13.66033, 28.96)"
    },
    {
      "name": "Obrien",
      "id": "10020",
      "recclass": "CI1",
      "mass (g)": "6000",
      "reclat": "44.11667",
      "reclong": "4.08333",
      "GeoLocation": "(44.11667, 4.08333)"
    },
    {
      "name": "Green",
      "id": "10021",
      "recclass": "L/LL4",
      "mass (g)": "2000",
      "reclat": "44.65",
      "reclong": "11.01667",
      "GeoLocation": "(44.65, 11.01667)"
    },
    {
      "name": "Bell",
      "id": "10022",
      "recclass": "L",
      "mass (g)": "625",
      "reclat": "2",
      "reclong": "22.66667",
      "GeoLocation": "(2.0, 22.66667)"
    },
    {
      "name": "Guillaume",
      "id": "10023",
      "recclass": "Eucrite-mmict",
      "mass (g)": "252",
      "reclat": "45.82133",
      "reclong": "6.01533",
      "GeoLocation": "(45.82133, 6.01533)"
    },
    {
      "name": "Bautista",
      "id": "10024",
      "recclass": "LL5",
      "mass (g)": "700",
      "reclat": "51.78333",
      "reclong": "-1.78333",
      "GeoLocation": "(51.78333, -1.78333)"
    },
    {
      "name": "Delgado",
      "id": "10025",
      "recclass": "L6",
      "mass (g)": "3200",
      "reclat": "36.23333",
      "reclong": "37.13333",
      "GeoLocation": "(36.23333, 37.13333)"
    },
    {
      "name": "Thompson",
      "id": "10026",
      "recclass": "H5",
      "mass (g)": "908",
      "reclat": "44.88333",
      "reclong": "8.75",
      "GeoLocation": "(44.88333, 8.75)"
    },
    {
      "name": "Fritter",
      "id": "10027",
      "recclass": "H4",
      "mass (g)": "9251",
      "reclat": "50.95",
      "reclong": "31.81667",
      "GeoLocation": "(50.95, 31.81667)"
    },
    {
      "name": "Fletcher",
      "id": "10028",
      "recclass": "L6",
      "mass (g)": "228000",
      "reclat": "45.26667",
      "reclong": "10.15",
      "GeoLocation": "(45.26667, 10.15)"
    },
    {
      "name": "Belin",
      "id": "10029",
      "recclass": "H5",
      "mass (g)": "32000",
      "reclat": "42.53333",
      "reclong": "-85.88333",
      "GeoLocation": "(42.53333, -85.88333)"
    },
    {
      "name": "Poeschel",
      "id": "10030",
      "recclass": "CV3",
      "mass (g)": "2000000",
      "reclat": "26.96667",
      "reclong": "-105.31667",
      "GeoLocation": "(26.96667, -105.31667)"
    }
  ]
}
```
</details>

# Dockerfile
The Dockerfile is a set of instructions given to the computer to create the correct doctor image. The Dockerfile is similar to a Makefile in the sense that is stores a set of instructions. Each command in the Dockerfile contributes to the neccessary developer environment needed. 

<details>
<summary>Show DockerFile </summary>

```terminal:


FROM centos:7.9.2009

RUN yum update -y && yum install -y python3
RUN pip3 install pytest==7.0.0

COPY ml_data_analysis.py /code/ml_data_analysis.py
COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py
COPY Meteorite_Landings.json /code/Meteorite_Landings.json

RUN chmod +rx /code/ml_data_analysis.py
RUN chmod +rx /code/test_ml_data_analysis.py
RUN chmod +rx /code/Meteorite_Landings.json

ENV PATH "/code:$PATH"
```
</details>







# Instructions:
1. [Pull and use your existing image on Docker Hub ](#introduction)
2. [Build an image from your Dockerfile](#paragraph1)
3. [Run the containerized code against the sample data inside the container](#subparagraph1)
4. [Run the containerized code against user-provided data that they may have found on the web](#paragraph2)
5. [Run the containerized test suite with pytest](#paragraph3)
6. [What input should look like](#paragraph4)

## Pull and use your existing image on Docker Hub  <a name="introduction"></a>
1. Go to my Dockerhub profile
https://hub.docker.com/repository/docker/bryan4027/ml_data_analysis

2. If you click on tags, you will see the latest version plus the older versions. The latest version is the option on the top. If you navigate to the right side of the screen, you will see a box with a copyable link which is the following
```python
docker pull bryan4027/ml_data_analysis:hw04
```
3. Paste the previous command into the terminal. When complete, the output will look like following:
```terminal
PS C:\Users\bacos> docker pull bryan4027/ml_data_analysis:hw04
hw04: Pulling from bryan4027/ml_data_analysis
2d473b07cdd5: Pull complete
5da5a235d053: Pull complete
34b124c5e311: Pull complete
262ce0fe5dcb: Pull complete
68e4890295e5: Pull complete
4095f3e4b287: Pull complete
cef545f9340f: Pull complete
e5defc447125: Pull complete
Digest: sha256:93c81c90384f3bbc41cf93b5ca031ad0eeeee287deaf988a5b78e77acf492416
Status: Downloaded newer image for bryan4027/ml_data_analysis:hw04
docker.io/bryan4027/ml_data_analysis:hw04

```
4.  Next, start the interactive shell by running the following!
```python
docker run --rm -it bryan4027/ml_data_analysis:hw04 /bin/bash
```
5.  Run the following two commands and the outputs should look like the following terminal output!
```python
[root@4e82e3d84ad6 /]# whoami
root
[root@4e82e3d84ad6 /]# pwd
/
```
6.  move into the file with the code! run the following
```python
cd code
```
7.  You are finally able to run the program with all neccesary system installations and files! Test it out by pasting the following into the terminal.
```python
python3 ml_data_analysis.py Meteorite_Landings.json
```
Your output should look like this: 
```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 83857.3

Hemisphere summary data:
There were 6  meteors found in the  Northern & Western Quadrant.
There were 21  meteors found in the  Northern & Eastern Quadrant.
There were 3  meteors found in the  Southern & Western Quadrant.
There were 0  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   L5  class was found  1 times.
The   H6  class was found  1 times.
... etc!
```

## Build an image from your Dockerfile <a name="paragraph1"></a>

1. Make sure you have all the files in this repository.
2. Paste the following into the terminal. Replace the <dockerusername> with your username and <version_tag_you_want_to_use> with the tag of your choosing. Example of mine below
```python
docker build -t <dockerusername>/ml_data_analysis:<version_tag_you_want_to_use> .
```
Example using my Docker account and tag:
```
docker build -t bryan4027/ml_data_analysis:hw04 .
```
Your output will look like the following.
<details>
<summary>Click to show output</summary>
   
```python:
[ba25389@isp02 homework04]$ docker build -t bryan4027/ml_data_analysis:hw04 .
Sending build context to Docker daemon  46.08kB
Step 1/10 : FROM centos:7.9.2009
 ---> eeb6ee3f44bd
Step 2/10 : RUN yum update -y && yum install -y python3
 ---> Using cache
 ---> d605a0dae43f
Step 3/10 : RUN pip3 install pytest==7.0.0
 ---> Using cache
 ---> f4be093b12b2
Step 4/10 : COPY ml_data_analysis.py /code/ml_data_analysis.py
 ---> 885dd5362f28
Step 5/10 : COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py
 ---> de44571f21d6
Step 6/10 : COPY Meteorite_Landings.json /code/Meteorite_Landings.json
 ---> 4229dd8dcb17
Step 7/10 : RUN chmod +rx /code/ml_data_analysis.py
 ---> Running in 4c4a8c38ee6a
Removing intermediate container 4c4a8c38ee6a
 ---> 8d55974bcf8a
Step 8/10 : RUN chmod +rx /code/test_ml_data_analysis.py
 ---> Running in c5e61f6d3d13
Removing intermediate container c5e61f6d3d13
 ---> 527ac6d58870
Step 9/10 : RUN chmod +rx /code/Meteorite_Landings.json
 ---> Running in b9b428f9a528
Removing intermediate container b9b428f9a528
 ---> fbaea8c9cd79
Step 10/10 : ENV PATH "/code:$PATH"
 ---> Running in 3fafa5399088
Removing intermediate container 3fafa5399088
 ---> f85ba3ea8785
Successfully built f85ba3ea8785
Successfully tagged bryan4027/ml_data_analysis:hw04
```
</details>

3.  Paste the following into the terminal. Replace the <dockerusername> with your username and <version_tag_you_want_to_use> with the tag of your choosing. Example of mine below
```python
docker run --rm -it <dockerusername>/ml_data_analysis:<version_tag_you_want_to_use> /bin/bash
```
Example using my Docker account and tag:
```
docker run --rm -it bryan4027/ml_data_analysis:hw04 /bin/bash
```
4.  Ensure the shell successfully opened by testing pwd and whoami commands and getting following output:
```python
[root@1ca2af4a9392 /]# pwd
/
[root@1ca2af4a9392 /]# whoami
root
```
5.  move into the file with the code! run the following
```python
cd code
```
6.  You are finally able to run the program with all neccesary system installations and files! Test it out by pasting the following into the terminal.
```python
python3 ml_data_analysis.py Meteorite_Landings.json
```
Your output should look like this: 
```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 83857.3

Hemisphere summary data:
There were 6  meteors found in the  Northern & Western Quadrant.
There were 21  meteors found in the  Northern & Eastern Quadrant.
There were 3  meteors found in the  Southern & Western Quadrant.
There were 0  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   L5  class was found  1 times.
The   H6  class was found  1 times.
... etc!
```

    
## Run the containerized code against the sample data inside the container <a name="subparagraph1"></a>    
    
1. First you must complete either steps 1 or 2, but at least one. Ensure you are logged into the interactive shell successfully opened by testing pwd and whoami commands and getting following output:
```python
[root@1ca2af4a9392 /]# pwd
/
[root@1ca2af4a9392 /]# whoami
root
```
2.  move into the file with the code! run the following
```python
cd code
```
3.  You are finally able to run the program with all neccesary system installations and files! Test it out by pasting the following into the terminal.
```python
python3 ml_data_analysis.py Meteorite_Landings.json
```
Your output should look like this: 
```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 83857.3

Hemisphere summary data:
There were 6  meteors found in the  Northern & Western Quadrant.
There were 21  meteors found in the  Northern & Eastern Quadrant.
There were 3  meteors found in the  Southern & Western Quadrant.
There were 0  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   L5  class was found  1 times.
The   H6  class was found  1 times.
... etc!
```
    
## Run the containerized code against user-provided data that they may have found on the web <a name="paragraph2"></a>
    
You may start off this process with either processes 1 or 2, but you MUST STOP before running the `docker run --rm -it bryan4027/ml_data_analysis:hw04 /bin/bash`. For the sake of an example, I will follow process 1. If you choose to follow step 2 and creat your own Image, skip to step 4 of this process.    
 
1. Go to my Dockerhub profile
https://hub.docker.com/repository/docker/bryan4027/ml_data_analysis

2. If you click on tags, you will see the latest version plus the older versions. The latest version is the option on the top. If you navigate to the right side of the screen, you will see a box with a copyable link which is the following
```python
docker pull bryan4027/ml_data_analysis:hw04
```
3. Paste the previous command into the terminal. When complete, the output will look like following:
```terminal
PS C:\Users\bacos> docker pull bryan4027/ml_data_analysis:hw04
hw04: Pulling from bryan4027/ml_data_analysis
2d473b07cdd5: Pull complete
5da5a235d053: Pull complete
34b124c5e311: Pull complete
262ce0fe5dcb: Pull complete
68e4890295e5: Pull complete
4095f3e4b287: Pull complete
cef545f9340f: Pull complete
e5defc447125: Pull complete
Digest: sha256:93c81c90384f3bbc41cf93b5ca031ad0eeeee287deaf988a5b78e77acf492416
Status: Downloaded newer image for bryan4027/ml_data_analysis:hw04
docker.io/bryan4027/ml_data_analysis:hw04

```
4.  Within the same folder where you have the rest of the neccesary files, paste the following command to download the file you want to test. 
```python
wget https://<your_webstite_url_here>.com
```  
    
5. Next, start the interactive shell by running the following! This command creates the image and loads all files in the current folder onto the container.
```python
docker run --rm -it -v $PWD:/data <username>/ml_data_analysis:<your_tag> /bin/bash
```
replace the <username> and <your_tag> with their respective names. Mine looks like this. 
```python
docker run --rm -it -v $PWD:/data bryan4027/ml_data_analysis:hw04 /bin/bash
```    
6.  Check the interactive shell successfully opened by running the following two commands and the outputs should look like the following terminal output!
```python
[root@4e82e3d84ad6 /]# whoami
root
[root@4e82e3d84ad6 /]# pwd
/
```
7.  move into the file with the code! run the following
```python
cd code
```
8.  You are finally able to run the program with all neccesary system installations and files! Test it out by pasting the following into the terminal. replace the <your_json_file_name> with your file name.
```python
python3 ml_data_analysis.py <your_json_file_name>.json
```
Your output should be in this format with different data: 
```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 83857.3

Hemisphere summary data:
There were 6  meteors found in the  Northern & Western Quadrant.
There were 21  meteors found in the  Northern & Eastern Quadrant.
There were 3  meteors found in the  Southern & Western Quadrant.
There were 0  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   L5  class was found  1 times.
The   H6  class was found  1 times.
... etc!
```
   

## Run the containerized test suite with pytest <a name="paragraph3"></a>
    
1. First you must complete either steps 1 or 2, but at least one. Ensure you are logged into the interactive shell successfully opened by testing pwd and whoami commands and getting following output:
```python
[root@1ca2af4a9392 /]# pwd
/
[root@1ca2af4a9392 /]# whoami
root
```
2.  move into the file with the code! run the following
```python
cd code
```
3.  You are finally able to run the program with all neccesary system installations and files! Test it out by pasting the following into the terminal.
```python
pytest
```
Your output should look like this: 
```python
[root@1ca2af4a9392 code]# pytest
============================ test session starts ============================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /code
collected 3 items

test_ml_data_analysis.py ...                                          [100%]

============================= 3 passed in 0.04s =============================
```

## What input should look like <a name="paragraph4"></a>    

The input data should be in JSON format. JSON is is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.
    
A JSON formatted file is essentially a list of dictionaries. It is formatted like the following: 

```python
   {
  "dictionary name": [
    {
      "key": "value",
      "key2": "value",
      "key3": "value",
    },
    {
      "key": "value",
      "key2": "value",
      "key3": "value",
    }, 
    ... etc
    
```
    
The following is an example of running our program with a sample JSON file from the web! The sample file is at https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json. Do not download the file yet.
    
    
You may start off this process with either processes 1 or 2, but you MUST STOP before running the `docker run --rm -it bryan4027/ml_data_analysis:hw04 /bin/bash`. For the sake of an example, I will follow process 1. If you choose to follow step 2 and creat your own Image, skip to step 4 of this process.    
 
1. Go to my Dockerhub profile
https://hub.docker.com/repository/docker/bryan4027/ml_data_analysis

2. If you click on tags, you will see the latest version plus the older versions. The latest version is the option on the top. If you navigate to the right side of the screen, you will see a box with a copyable link which is the following
```python
docker pull bryan4027/ml_data_analysis:hw04
```
3. Paste the previous command into the terminal. When complete, the output will look like following:
```terminal
PS C:\Users\bacos> docker pull bryan4027/ml_data_analysis:hw04
hw04: Pulling from bryan4027/ml_data_analysis
2d473b07cdd5: Pull complete
5da5a235d053: Pull complete
34b124c5e311: Pull complete
262ce0fe5dcb: Pull complete
68e4890295e5: Pull complete
4095f3e4b287: Pull complete
cef545f9340f: Pull complete
e5defc447125: Pull complete
Digest: sha256:93c81c90384f3bbc41cf93b5ca031ad0eeeee287deaf988a5b78e77acf492416
Status: Downloaded newer image for bryan4027/ml_data_analysis:hw04
docker.io/bryan4027/ml_data_analysis:hw04

```
4.  Within the same folder where you have the rest of the neccesary files, paste the following command to download the file you want to test. For this example we are using sample data.
```python
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```  
    
5. Next, start the interactive shell by running the following! This command creates the image and loads all files in the current folder onto the container.
```python
docker run --rm -it -v $PWD:/data <username>/ml_data_analysis:<your_tag> /bin/bash
```
replace the <username> and <your_tag> with their respective names. Mine looks like this. 
```python
docker run --rm -it -v $PWD:/data bryan4027/ml_data_analysis:hw04 /bin/bash
```    
6.  Check the interactive shell successfully opened by running the following two commands and the outputs should look like the following terminal output!
```python
[root@4e82e3d84ad6 /]# whoami
root
[root@4e82e3d84ad6 /]# pwd
/
```
7.  move into the file with the code! run the following
```python
cd code
```
8.  You are finally able to run the program with all neccesary system installations and files! Test it out by pasting the following into the terminal. replace the <your_json_file_name> with your file name.
```python
python3 ml_data_analysis.py ML_Data_Sample.json
```
Your output should be in this format (with different data if you try another file!) 
```python
Summary data following meteorite analysis:

Average mass of 30 meteor(s): 5081.37

Hemisphere summary data:
There were 86  meteors found in the  Northern & Western Quadrant.
There were 71  meteors found in the  Northern & Eastern Quadrant.
There were 69  meteors found in the  Southern & Western Quadrant.
There were 74  meteors found in the  Eastern & Western Quadrant.

Class summary data:
The   H4  class was found  22 times.
The   L6  class was found  18 times.

... etc!
```
    
    
