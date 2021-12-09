# Ethan's Aon Backend Test

This is a simple API that will return fibanocci numbers. Postgres is used to cache the results.

## Prerequisites

- Docker and Docker Compose are installed

## Quickstart

## Testing

Tests are located in `tests` root level directory. Execute them by running `python3 -m unittest`

## CLI

A simple CLI tool exists in `/src/cli` that allows making requests against the API.

This tool assumes that the API services are up and running on your localhost.

```
docker run -it --rm --network="host" cli calc-fib-sequence 3
```