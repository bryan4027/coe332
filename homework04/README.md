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

# Run the containerized code against the sample data inside the container
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

# Run the containerized code against user-provided data that they may have found on the web
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

# Run the containerized test suite with pytest

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
6.  
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
