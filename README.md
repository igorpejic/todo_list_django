https://github.com/igorpejic/todo_list_django/assets/6241267/d96e69d5-5dcb-4bd6-839b-131efeb7a98c


## Running using docker-compose

Requirements:
- [Docker](https://docs.docker.com/engine/install/)
- [Docker compose](https://docs.docker.com/compose/install/)

Before running docker-compose, in docker-compose.yml get your [OpenWeather API](https://openweathermap.org/api) key.

Then run:

`OPENWEATHER_API_KEY=your_key docker compose up`

On first run, the database will be populated with countries and cities so will take longer (~10 minutes depending on your internet speed) to start-up. 
(In docker-compose you will see: `Building region index: 0it [00:00, ?it/s])`. At this step you should wait.

On the next docker compose up, this will be much faster as the migration has been executed on the first run.


## Running locally

- Python (version as specified in the Dockerfile[docker/Dockerfile])
- [poetry](https://python-poetry.org/)
- [PostgreSQL 12](https://www.postgresql.org/download/)
- [PostGIS](https://postgis.net/)
- [GeoDjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/#setting-up)


### Python Requirements

Open a terminal at the project root and install the requirements for local development:
```
    $ poetry install
```

Enter a virtual environment with the dependencies available:
```
    $ poetry shell
```


### How does it work?

Every time a non-finished TODO is rendered, we check if this model's weather data is already present in the cache (cache-aside loading), and if not, the OpenWeather API is queried. The cache expiration can be tuned to lower the load on the OpenWeather API but will produce staler results.

For selection of user location we are leveraging [django-cities](https://github.com/coderholic/django-cities/) to populate a list of possible countries and cities.
Based on the city selected we obtain the latitude and longitude that we pass to OpenWeather API to obtain the temperature and the overall weather condition.
Using the weather condition, we color the task background.

For finished TODOs, we are saving the weather data in the db and fetching that recorded data.

### Further improvements

- [ ] Replace local Django in-memory cache with Redis
