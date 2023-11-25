## Running using docker-compose

Requirements:
- [Docker](https://docs.docker.com/engine/install/)
- [Docker compose](https://docs.docker.com/compose/install/)

docker-compose up


## Running locally

- Python (version as specified in the Dockerfile[docker/Dockerfile])
- [poetry](https://python-poetry.org/)
- [PostgreSQL 12](https://www.postgresql.org/download/)
- [PostGIS](https://postgis.net/)
- [GoeDjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/#setting-up)


### Python Requirements

Open a terminal at the project root and install the requirements for local development:
```
    $ poetry install
```

Enter a virtual environment with the dependencies available:
```
    $ poetry shell
```
