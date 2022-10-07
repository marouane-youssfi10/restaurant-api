### Restaurant API's
A Detailed restaurant API built with Django, Docker,Celery,Redis, Nginx, Django Rest Framework and more...

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
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1
make build
make up
