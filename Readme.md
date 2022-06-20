### `docker-compose`

```bash
use this command to run dockerfile
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1
docker compose -f local.yml up --build -d --remove-orphans
docker compose -f local.yml up