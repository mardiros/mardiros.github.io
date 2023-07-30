install:
    poetry install

build:
    poetry run sphinx-build . public

black:
    poetry run isort .
    poetry run black .

gh-pages:
    poetry export -f requirements.txt -o requirements.txt --without-hashes

view:
    xdg-open public/index.html

clean:
    rm -rf public