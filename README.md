# Mardiros' Personal Projects

Hey, I'm Mardiros, and I'm a programmer. I mainly work with Python, but occasionally I use Rust.

I also combine both languages using PyO3.

Below is a curated list of personal projects that I am actively developing, maintaining or still using.

All those projects are opensource and code is available at Github. Python libraries are also published on PyPI.

## Python Libraries

### Fastlife

[fastlife](https://mardiros.github.io/fastlife/) is an asynchronous web framework built on FastAPI, HTMX, and JinjaX.
The goal is to facilitate rapid web application development.

The documentation is available at: [https://mardiros.github.io/fastlife/](https://mardiros.github.io/fastlife/).

The project is currently in development; I plan to replace JinjaX by XComponent, the next library on the list.

### XComponent

[XComponent](https://mardiros.github.io/xcomponent/) is a template engine inspired by JSX for Python.

The core of the template engine is written in Rust using PyO3 bindings.

This template engine's API differs from existing ones because all templates are written within Python functions. There is no separate template file.

The documentation is available at: [https://mardiros.github.io/xcomponent/](https://mardiros.github.io/xcomponent/).

### messagebus

[messagebus](https://mardiros.github.io/messagebus/) is a library for constructing an event-driven architecture in Python. It supports both synchronous and asynchronous code based on asyncio.

The documentation is available at: [https://mardiros.github.io/messagebus/](https://mardiros.github.io/messagebus/).

### Turşu

[turşu](https://mardiros.github.io/tursu/) is a Gherkin framework for Python.

It compiles Gherkin scenarios into a pytest test suite using the Python AST.

It allows the use of pytest fixtures within step definitions.

The documentation is available at: [https://mardiros.github.io/tursu/](https://mardiros.github.io/tursu/).

### Blacksmith

[blacksmith](https://mardiros.github.io/blacksmith/) is a library for building robust microservices architecture based on REST APIs in Python. It supports both synchronous and asynchronous code based on asyncio.

It is not an HTTP client; rather, it includes features like service discovery, metrics, circuit breakers, and more.

The documentation is available at: [https://mardiros.github.io/blacksmith/](https://mardiros.github.io/blacksmith/).

The project is stable and mature.

Some web framework integrations exist as extra packages:

- [dj-blacksmith - blacksmith for Django](https://mardiros.github.io/dj-blacksmith/)
- [pyramid-blacksmith - blacksmith for Pyramid](https://mardiros.github.io/pyramid-blacksmith/)

### Purgatory

[purgatory](https://mardiros.github.io/purgatory/) is a circuit breaker implementation for Python.
It supports both synchronous and asynchronous code based on asyncio.

The documentation is available at: [https://mardiros.github.io/purgatory/](https://mardiros.github.io/purgatory/).

The project is stable and mature.

### lastuuid

[lastuuid](https://mardiros.github.io/lastuuid/) is a small library to generate UUIDv7 that works with Pydantic.

The project does not implement UUIDv7 itself; it is a binding to UUIDv7 in Rust using PyO3.

### envsub

[envsub](https://github.com/mardiros/envsub/) is a library to substitute environment variables on the fly while reading a file stream.

It has been implemented in Rust and binds with PyO3 to run blazingly fast.

The documentation is available at: [https://mardiros.github.io/envsub/](https://mardiros.github.io/envsub/).

### plaster-yaml

[plaster-yaml](https://github.com/mardiros/plaster-yaml/) is a library to configure a Pyramid app using YAML (or JSON) format instead of .ini files.

It also uses envsub to inject secrets or any other settings on the fly while reading the configuration, maximizing flexibility and keeping the loaded Python object as a single source of truth for the configuration.

### celery-yaml

[celery-yaml](https://github.com/mardiros/celery-yaml/) is a library to configure a Celery app using a YAML file instead of a Python module.

It also uses envsub to inject secrets or any other settings on the fly while reading the configuration, maximizing flexibility and keeping the loaded Python object as a single source of truth for the configuration.

### Pydantricks

[Pydantricks](https://mardiros.github.io/pydantricks/) is a library to build fake Pydantic models. It uses Faker under the hood to ensure clean fake models.

The documentation is available at: [https://mardiros.github.io/pydantricks/](https://mardiros.github.io/pydantricks/).

## Rust Libraries and Tools

### Rustaman

[rustaman](https://github.com/mardiros/rustaman/) is an HTTP client template designed for everyday queries.

It's similar to Postman but not designed as a clickodrome. HTTP queries are templatized with Mustache.

### Cabot

[cabot](https://github.com/mardiros/cabot/) is an HTTP CLI client similar to curl.

This lib is not actively maintained.

### Bearer

[bearer](https://github.com/mardiros/bearer/) is an OAuth2 authorization token made for CLI.

This lib is not actively maintained too.
