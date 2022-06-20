### `docker-compose`

```bash
use this command to run dockerfile

export DATABASE_URL=postgres://user:password@127.0.0.1:5432/db_name
docker compose -f local.yml up --build -d --remove-orphans