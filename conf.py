import pathlib
import tomllib
from datetime import datetime

here = pathlib.Path(__file__).parent.absolute()


# -- Project information -----------------------------------------------------
def _get_project_meta():
    with open("./pyproject.toml", "rb") as pyproject:
        return tomllib.load(pyproject)["project"]


pkg_meta = _get_project_meta()
project = str(pkg_meta["description"])
author = f"{pkg_meta['authors'][0]['name']} <{pkg_meta['authors'][0]['email']}>"
copyright = pkg_meta["authors"][0]["name"]

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
