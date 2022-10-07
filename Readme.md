# Restaurant API's
A Detailed restaurant API built with Django, Docker,Celery,Redis, Nginx, Django Rest Framework and more...

### Implementation
- Django REST Framework function-based views
- Django REST Framework class-based views

Each of the implementations are tested and documented with OpenAPI (Swagger UI). 

### Local development
This project is heavily focused on the process of setting up the development environment. This project has been tested and developed on:

- Ubuntu 20.04
- macOS 11.4 (Apple Silicon)

### Makefile

A Makefile is included in the root of the project to document. This file helps to document each step of the local development environment and deployment process.

### Developing with virtual environments

The application can be developed with a virtual environment locally. This requires starting postgres and redis services locally. Alternatively, postgres, redis and other supporting services can be started with a docker-compose file that exposes the services on localhost.

### Developing with docker

Docker is a popular choice for developing and deploying applications, including Django. docker-compose can be used to run the application and dependent services in containers. See local.yml in the root directory for more details.

The docker-compose file contains the following services:

- postgres: Postgres service
- redis: Redis service
- pgadmin: Postgres admin service
- backend: main Django web application
- celery_default: celery worker that processes the default queue
- mailhog: a local SMTP server for testing

### Continuous Intergration

tools are used for running unit tests and code quality checks on each commit. These include:

- GitHub Actions

Continuous integration checks that all unit tests pass and that code is formatted correctly. Unit tests run the Python code in a simulated environment that contains the dependent services (postgres and redis). The following tools are used in CI:

- flake8
- black
- pytest

### Setup Project

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/marouane-youssfi10/restaurant-api.git
$ cd restaurant-api
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m pip install virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements/local.txt
```

Create *restaurant-api/django-local.env* file to store the passwords

```bash
SIGNING_KEY=
CELERY_BROKER = redis://redis:6379/0
CELERY_BACKEND = redis://redis:6379/0
DOMAIN = localhost:8080
EMAIL_PORT = 1025 
CELERY_FLOWER_USER = your_user
CELERY_FLOWER_PASSWORD = your_password
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 587
EMAIL_HOST_USER = your_mail
EMAIL_HOST_PASSWORD = your_password
EMAIL_USE_TLS = True
```

use this command to run dockerfile
```bash
# This is required to add support for some ARGs defined in Dockerfile
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1
make build
make up
