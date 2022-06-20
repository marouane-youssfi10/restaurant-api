help:
	@echo "docker-compose commands:"
	@echo "    make lint:         Run pre-commit hooks"
	@echo "    make rm: 		  Removes all docker containers running"
	@echo "    make up: 		  Up all services - Starts all services"
	@echo "    make bash: 		  Bash into application container"
	@echo "    make ps:			  list containers/services"
	@echo "	   make restart:      restart (removes all services and restart them -- without rebuilding)"
	@echo "    make shell_plus:   access shell"
	@echo "	   make build:		  build (usually, requires to build when changes happen to the Dockerfile or docker-compose.yml)"
	@echo "    make bash: 		  open bash console in the app service"
	@echo "    make test: 		  run application unit tests"
	@echo "    make shell_plus:   access shell"


lint:
	docker-compose -f local.yml run --rm api pre-commit run --all-files

build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up

upd:
	docker compose -f local.yml up -d

rm:
	docker compose -f local.yml down && docker compose -f local.yml rm -f

down:
	docker compose -f local.yml down

ps:
	docker-compose ps

bash:
	docker compose f local.yml run --rm api bash

show_logs:
	docker compose -f local.yml logs

migrate:
	docker compose -f local.yml run --rm api python3 manage.py migrate

migrations:
	docker compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:
	docker compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python3 manage.py createsuperuser

test:
	docker-compose -f local.yml run --rm api pytest

clear_database:
	docker-compose -f local.yml down --rmi all --volumes

shell:
	docker compose -f local.yml run --rm api python manage.py shell

restart:
	make rm && make up

flake8:
	docker compose -f local.yml exec api flake8 .

black:
	docker compose -f local.yml exec api black --exclude=migrations .