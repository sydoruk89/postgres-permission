# Permissions & Postgresql

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

Django REST Framework to create an API, then “containerize” it with Docke and adding Permissions and Postgresql Database.

## Architecture

* Python 3.8.3
* Poetry
* Django
* Docker
* Postgres 11

## Usage 
### Features - Django REST Framework
* Make your site a DRF powered API as you did in previous lab.
Adjust project’s permissions so that only authenticated user’s have access to API.
* Add a custom permission so that only author of blog post can update or delete it.
* Add ability to switch user’s directly from browsable API.

### Features - Docker
* create Dockerfile based off python:3.8-slim
* create docker-compose.yml to run Django app as a web service.
* enter docker-compose up --build to start your site
* add postgres 11 as a service
