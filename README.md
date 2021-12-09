# Ethan's Aon Backend Test

This is a simple API that will return fibanocci numbers. Postgres is used to cache the results, and log requests made to the API.

Two separate applications are contained within this repository's `src/`:
* **api** -- main application
* **cli** -- console app that allows queries to be made against api (similar to how one would typically query w/ postman)

# API

### Prerequisites

- Docker and Docker Compose are installed
- Internet access (to DockerHub)

### Quickstart

Run `docker-compose build && docker-compose up -d` from the root of this repository to start services. Docker Compose will handle starting a development postgres server, and once it's started, a development API will spin up for you to make requests against.

It should be running on `localhost:5000` and postgres on `localhost:5432` (make sure these ports are available!)

Once both the API and postgres services are running and healthy, you an execute requests using the included CLI application (see below for more details); or a tool like postman, insomnia, etc.

### Endpoint Overview

/fibonacci/<count> -- returns <count> number of finonacci's

/fibonacci/requests/<month-year> -- returns api request statistics for the given month and year

### Testing

Tests are located in the api project. Execute them by running `python3 -m unittest`.

The main application logic has test coverage. 

### Environment Variables

When running/developing the API outside of docker, the following environment variables are expected:

- DB_HOST (hostname of Postgres instance)
- DB_USER
- DB_PASS

# CLI

A simple CLI tool exists in `/src/cli` that allows making requests against the API.

This tool assumes that the API services are up and running on your localhost.

You can run this CLI using docker, shown below:

```
cd src/cli
docker build -t cli .
docker run -it --rm --network="host" cli <function> <arguments>
```

Alternatively, if you have Python 3.8 or newer, you can execute the application directly:

```
cd src/cli
pip install -r packages.txt
python3 main.py <function> <arguments>
```

# TODO / Shortcomings

This was intended to be a simple implementation of the given specs. Some points of improvement could include:

- Use modules to split out tests into a separate "project" 
- Refactor services to allow dependency injection -- would open up more testing possibilities
- Probably quite a bit more? (I haven't worked in python before, and there are likely many best practices and techniques I have to learn)
