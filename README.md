# Serverless AWS Data PipeLine

## Description

***
Our project aims to create a serverless aws Lambda application that describes a data pipe line for extracting and loggin application response times 
***
## Requirements

> AWS Iam Account

> GitHub Account

> Lunix/Ubuntu based Operating System Distribution

## Configuration

***

Steps to follow to configure & excecute the program in Ubuntu based linux distributions

* Clone Repository
```
$ git clone https://github.com/DanielR-spec/Serverless.git

```
* setUp GitHub Secrets

* Generate Ci/Cd Deployment workflow file, follow the GitHub Actions FrameWork

* Initialize AWS credentials in OS
```
$ sudo apt-get install awscli
$ aws configure

```
* Create & activate virtual enviroment
```
$ python -m venv /path/to/new/virtual/environment
$ source /path/to/venv/bin/activate
```
* Install requirement (packages)
```
$ cd /path/to/cloned/repository                     
$ pip install -r requirements.txt
```
* Excecute Lambda Function
```
$ cd /serverless/path/to/lambda/file
$ python lambda_name.py             
```
***
