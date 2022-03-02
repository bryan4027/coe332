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
4.  
```python
pip3 install pytest==7.0.0
```
5.  
```python
docker run --rm -it -v $PWD:/code centos:7.9.2009 /bin/bash
```

## Build an image from your Dockerfile <a name="paragraph1"></a>
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

## Run the containerized code against the sample data inside the container <a name="subparagraph1"></a>
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

## Run the containerized code against user-provided data that they may have found on the web <a name="paragraph2"></a>
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

