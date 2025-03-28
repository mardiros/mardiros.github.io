# Mardiros' Personal Projects.

Hi, I am mardiros, and I do programming. Mostly in python, rust.

## Python Libraries

### Turşu

[turşu](https://mardiros.github.io/tursu/) is a Gherkin framework for python.

It compiles Gherkin scenario to a pytest tests suite using python AST.

It let you using pytest fixtures inside steps commands.

The documentation is avalable at: [https://mardiros.github.io/fastlife/](https://mardiros.github.io/tursu/).

The project is in development

### Fastlife

[fastlife](https://mardiros.github.io/fastlife/) is an asynchronous web framework based on fastapi.
The idea is to build web application quickly.

The documentation is avalable at: [https://mardiros.github.io/fastlife/](https://mardiros.github.io/fastlife/).

The project is in development

### Blacksmith

[blacksmith](https://mardiros.github.io/blacksmith/) is a library to build a solid
microservices architecture based on REST API in Python 3. It support both synchronous
and asynchronous code based on asyncio.

It is not an http client, it embed some features like service discovery, metrics,
circuit breaker, and more.

The documentation is avalable at: [https://mardiros.github.io/blacksmith/](https://mardiros.github.io/blacksmith/).

The project is stable and mature.

Some web framework integration exists that are extra packages:

- [dj-blacksmith - blacksmith for Django](https://mardiros.github.io/dj-blacksmith/)
- [pyramid-blacksmith - blacksmith for Pyramid](https://mardiros.github.io/pyramid-blacksmith/)

### messagebus

[messagebus](https://mardiros.github.io/messagebus/) is a library to build an event driven
architecture in Python 3. It support both synchronous and asynchronous code based on asyncio.

The documentation is avalable at: [https://mardiros.github.io/messagebus/](https://mardiros.github.io/messagebus/).

### Pydantricks

[Pydantricks](https://mardiros.github.io/pydantricks/) is a library to build fake pydantic
models. It use Faker under the hood, to have clean fake models.

The documentation is avalable at: [https://mardiros.github.io/pydantricks/](https://mardiros.github.io/pydantricks/).

### Purgatory

[purgatory](https://mardiros.github.io/purgatory/) is a circuit breaker implementation for Python 3.
It support both synchronous and asynchronous code based on asyncio.

The documentation is avalable at: [https://mardiros.github.io/purgatory/](https://mardiros.github.io/purgatory/).

The project is stable and mature.

### lastuuid

[lastuuid](https://mardiros.github.io/lastuuid/) is a small to generate UUIDv7 that works with Pydantic.

The project is does not implement uuid7, it is a binding to uuid7 in rust using pyo3.

### envsub

[envsub](https://github.com/mardiros/envsub/) is library to substitute environment variable on the fly
while reading a file stream.

It has been implemented in rust and bind with pyo3 to run blazingly fast.

The documentation is avalable at: [https://mardiros.github.io/envsub/](https://mardiros.github.io/envsub/).

### plaster-yaml

[plaster-yaml](https://github.com/mardiros/plaster-yaml/) is library to configure a pyramid app

in a yaml (or json) format instead of .ini file.

It also use envsub in order to inject secrets or any other settings replaced on the fly while
reading the configuration. It let maximum of flexibility and keep the loaded python object
as a single point of truth for the configuration.

### celery-yaml

[celery-yaml](https://github.com/mardiros/celery-yaml/) is a library to configure a celery app
using a yaml file instead of python module.

It also use envsub in order to inject secrets or any other settings replaced on the fly while
reading the configuration. It let maximum of flexibility and keep the loaded python object
as a single point of truth for the configuration.

## Rust libraries en tools

### Rustaman

[rustaman](https://github.com/mardiros/rustaman/) is a HTTP client template makes for
day to day query.

It's like a postman but not designed as a clickodrome. HTTP query templatized with
mustache.

### Cabot

[cabot](https://github.com/mardiros/cabot/) is a HTTP CLI client like curl, but it is
also a library, like reqwest.

### Bearer

[bearer](https://github.com/mardiros/bearer/) is a oauth2 authorization token made
for CLI.
