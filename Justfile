install:
    uv sync --frozen

build:
    uv run sphinx-build . public

fmt:
    uv run ruff check --fix .
    uv run ruff format src tests

view:
    xdg-open public/index.html

clean:
    rm -rf public
