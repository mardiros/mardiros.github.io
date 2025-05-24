# Mardiros' Personal Projects.

Hi, I am mardiros, and I do programming. Mostly in python, sometime in rust.

Here is a curated list of personal projects that I develop and try maintain.

## Python Libraries

### Fastlife

[fastlife](https://mardiros.github.io/fastlife/) is an asynchronous web framework based on fastapi, htmx and JinjaX.
The idea is to build web application quickly.

The documentation is available at: [https://mardiros.github.io/fastlife/](https://mardiros.github.io/fastlife/).

The project is in development

### XComponent

[XComponent](https://mardiros.github.io/xcomponent/) is a template engine inspired by JSX for python.

The core of the template engine is written in rust using pyo3 binding.

The API of this template differs to any existing template engine since all the template are written in
python functions. There is no way to define a template distinct file.

The documentation is available at: [https://mardiros.github.io/xcomponent/](https://mardiros.github.io/xcomponent/).


### messagebus

[messagebus](https://mardiros.github.io/messagebus/) is a library to build an event driven
architecture in Python. It support both synchronous and asynchronous code based on asyncio.

The documentation is available at: [https://mardiros.github.io/messagebus/](https://mardiros.github.io/messagebus/).

### Turşu

[turşu](https://mardiros.github.io/tursu/) is a Gherkin framework for python.

It compiles Gherkin scenario to a pytest tests suite using python AST.

It let you use pytest fixtures inside step definitions.

The documentation is available at: [https://mardiros.github.io/tursu/](https://mardiros.github.io/tursu/).

### Blacksmith

[blacksmith](https://mardiros.github.io/blacksmith/) is a library to build a solid
microservices architecture based on REST API in Python. It support both synchronous
and asynchronous code based on asyncio.

It is not an http client, it embed some features like service discovery, metrics,
circuit breaker, and more.

The documentation is available at: [https://mardiros.github.io/blacksmith/](https://mardiros.github.io/blacksmith/).

The project is stable and mature.

Some web framework integration exists that are extra packages:

- [dj-blacksmith - blacksmith for Django](https://mardiros.github.io/dj-blacksmith/)
- [pyramid-blacksmith - blacksmith for Pyramid](https://mardiros.github.io/pyramid-blacksmith/)

### Purgatory

[purgatory](https://mardiros.github.io/purgatory/) is a circuit breaker implementation for Python.
It support both synchronous and asynchronous code based on asyncio.

The documentation is available at: [https://mardiros.github.io/purgatory/](https://mardiros.github.io/purgatory/).

The project is stable and mature.

### lastuuid

[lastuuid](https://mardiros.github.io/lastuuid/) is a small to generate UUIDv7 that works with Pydantic.

The project is does not implement uuid7, it is a binding to uuid7 in rust using pyo3.

### envsub

[envsub](https://github.com/mardiros/envsub/) is library to substitute environment variable on the fly
while reading a file stream.

It has been implemented in rust and bind with pyo3 to run blazingly fast.

The documentation is available at: [https://mardiros.github.io/envsub/](https://mardiros.github.io/envsub/).

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

### Pydantricks

[Pydantricks](https://mardiros.github.io/pydantricks/) is a library to build fake pydantic
models. It use Faker under the hood, to have clean fake models.

The documentation is available at: [https://mardiros.github.io/pydantricks/](https://mardiros.github.io/pydantricks/).

## Rust libraries en tools

### Rustaman

[rustaman](https://github.com/mardiros/rustaman/) is a HTTP client template makes for
day to day query.

It's like a postman but not designed as a clickodrome. HTTP query templatized with
mustache.

### Cabot

[cabot](https://github.com/mardiros/cabot/) is a HTTP CLI client like curl.

### Bearer

[bearer](https://github.com/mardiros/bearer/) is a oauth2 authorization token made
for CLI.
