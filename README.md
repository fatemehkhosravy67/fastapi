# About The Project

This project about a shopping store.

FastAPI

peewee-orm 

jwt token

## Introduction

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features that I like in FastApi are:

Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.

Fast to code: Increase the speed to develop features by about 200% to 300%. 

Fewer bugs: Reduce about 40% of human (developer) induced errors. 

Easy: Designed to be easy to use and learn. Less time reading docs.

Robust: Get production-ready code. With automatic interactive documentation.

Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

This Repository is aimed at helping those who are working on e-commerce applications.

## Getting Started


#### Prerequisites
  - [Python](https://www.python.org/downloads/) is installed 


#### Run the project
1.git clone

        git clone https://github.com/fatemehkhosravy67/fastapi.git


2.create python virtualenv

        python3 -m venv venv

3.active python virtualenv

4.set **JWT_SECRET** and create an environment file called .env in the base directory:
The secret in the environment file should be substituted with something stronger and should not be disclosed. For example:
import os
import binascii
binascii.hexlify(os.urandom(24))

The secret key is used for encoding and decoding JWT strings.

The algorithm value on the other hand is the type of algorithm used in the encoding process.

.env:

JWT_SECRET=deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f

MAIL_USERNAME=Fa

MAIL_PASSWORD=1234@Fa

MAIL_FROM=myname@gmail.com

MAIL_PORT=587

MAIL_SERVER=smtp.gmail.com

MAIL_TLS=True

MAIL_SSL=False



5.install packages

        pip install -r requirements.txt

## Usage

        uvicorn main:app --reload


You can visit localhost:8000/docs for swagger.