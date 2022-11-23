## Installation

[Install `Docker Compose`](https://docs.docker.com/compose/install/).

### Configuration

Copy the `.env.template` file to `.env`. Set the settings you need in the `.env` file.

### Run

```bash
docker compose build
docker compose run --rm django python3 manage.py makemigrations
docker compose run --rm django python3 manage.py migrate
docker compose run --rm django python3 manage.py createsuperuser
docker compose up
```

Open [https://127.0.0.1:8000/admin](https://127.0.0.1:8000/admin) and add items.

Open [https://127.0.0.1:8000/item/"id"](https://127.0.0.1:8000//item/"id") where "id" is item id.
