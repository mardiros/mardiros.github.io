import pathlib
from datetime import datetime

import tomlkit

here = pathlib.Path(__file__).parent.absolute()


# -- Project information -----------------------------------------------------
def _get_project_meta():
    with open(here / "pyproject.toml", "r") as pyproject:
        file_contents = pyproject.read()

    return tomlkit.parse(file_contents)["tool"]["poetry"]  # type: ignore


pkg_meta = _get_project_meta()
project = str(pkg_meta["description"])  # type: ignore
copyright = f"2023-{datetime.utcnow().year}, unencumbered software released"
author = ", ".join(pkg_meta["authors"])  # type: ignore

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

language = "en"
extensions = [
    "myst_parser",
]

source_suffix = [".rst", ".md"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "furo"
html_static_path = []
html_css_files = []
html_theme_options = {}
