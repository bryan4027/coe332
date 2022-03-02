# This folder belongs to Bryan Acosta's homework 4.
Eid ba25389. TACC id: ba25389.






# Analyzing Mar's Rover's Collected Data
The purpose of this project is to read in a JSON file of the collected data, analyze it, and determine if the water is safe for sample testing. It determines this based off the 5 most recent data points. This project enhances my skills with JSON manipulation, huge list manipulation, Python organization, documentation, logging, unit testing, and more.

<details>
<summary>Show python script 2: test_analyze_water.py </summary>
Python

```python:


if __name__ == '__pytest__':
    pytest()
```
</details>




# Instructions:
1. [Pull and use your existing image on Docker Hub ](#introduction)
2. [Build an image from your Dockerfile](#paragraph1)
3. [Run the containerized code against the sample data inside the container](#subparagraph1)
4. [Run the containerized code against user-provided data that they may have found on the web](#paragraph2)
5. [Run the containerized test suite with pytest](#paragraph3)

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
    
You may start off this process with either processes 1 or 2, but you MUST STOP before running the `command`. For the sake of an example, I will follow process 1. If you choose to follow step 2 and creat your own Image, skip to step BLANK of this process    
 
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
1. 
```python
docker run --rm -it -v $PWD:/code centos:7.9.2009 /bin/bash
```
2. 
```python
yum update
```
3.  
```python
yum install python3
```
4.  
```python
pip3 install pytest==7.0.0
```
5.  
```python
docker run --rm -it -v $PWD:/code centos:7.9.2009 /bin/bash
```



```python
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
7.  
```python
docker build -t <dockerhubusername>/<code>:<version> .
```
8.  
```python
docker build -t bryan4027/ml_data_analysis:1.0 .
```

