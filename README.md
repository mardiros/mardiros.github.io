# Mardiros' Personal Projects.

As a developper, I want to to learn and share my knowledge, so that I make progress.

[![Doc](https://github.com/mardiros/mardiros.github.io/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/mardiros/mardiros.github.io/actions/workflows/gh-pages.yml)

Please [visit https://mardiros.github.io/](https://mardiros.github.io/) for the full
version.

## Python Libraries

### Blacksmith

[blacksmith](https://mardiros.github.io/blacksmith/) is a library to build a solid
microservices architecture based on REST API in Python 3. It support both synchronous
and asynchronous code based on asyncio.

It is not an http client, it embed some features like service discovery, metrics,
circuit breaker, and more.

The full documentation is here: [https://mardiros.github.io/blacksmith/](https://mardiros.github.io/blacksmith/).

The project is stable and mature.

Some web framework integration exists that are extra packages:

* [dj-blacksmith - blacksmith for Django](https://mardiros.github.io/dj-blacksmith/)
* [pyramid-blacksmith - blacksmith for Pyramid](https://mardiros.github.io/pyramid-blacksmith/)


### Fastlife

[fastlife](https://mardiros.github.io/fastlife/) is an asynchronous web framework based on fastapi.
The  idea is to build web application quickly.

The full documentation is here: [https://mardiros.github.io/fastlife/](https://mardiros.github.io/fastlife/).

The project is in development


### messagebus

[messagebus](https://mardiros.github.io/messagebus/) is a library to build an event driven
architecture in Python 3. It support both synchronous and asynchronous code based on asyncio.

The full documentation is here: [https://mardiros.github.io/messagebus/](https://mardiros.github.io/messagebus/).

This project is not production ready yet.


### Purgatory

[purgatory](https://mardiros.github.io/purgatory/) is a circuit breaker implementation for Python 3.
It support both synchronous and asynchronous code based on asyncio.


The full documentation is here: [https://mardiros.github.io/purgatory/](https://mardiros.github.io/purgatory/).

The project is stable and mature.


### lastuuid

[lastuuid](https://mardiros.github.io/lastuuid/) is a small to generate UUIDv7 that works with Pydantic.

The project is does not implement uuid7, it is a binding to uuid7 in rust using pyo3.


### subenv

[subenv](https://github.com/mardiros/subenv/) is library to substitute environment variable on the fly
while reading a file stream.

It has been implemented in rust and bind with pyo3 to run blazingly fast.


### plaster-yaml

[plaster-yaml](https://github.com/mardiros/plaster-yaml/) is library to configure a pyramid app

in a yaml (or json) format instead of .ini file.

It also use subenv in order to inject secrets or any other settings replaced on the fly while
reading the configuration. It let maximum of flexibility and keep the loaded python object
as a single point of truth for the configuration.

### celery-yaml

[celery-yaml](https://github.com/mardiros/celery-yaml/) is a library to configure a celery app
using a yaml file instead of python module.

It also use subenv in order to inject secrets or any other settings replaced on the fly while
reading the configuration. It let maximum of flexibility and keep the loaded python object
as a single point of truth for the configuration.
