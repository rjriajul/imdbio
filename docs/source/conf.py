from importlib.metadata import version as _v

project = "imdbio"
copyright = "2026, rjriajul"
author = "rjriajul"
release = _v("imdbio")
del _v

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

autosummary_generate = True
napoleon_use_rtype = False
napoleon_use_param = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "imdbio"
html_baseurl = "https://rjriajul.github.io/imdbio/"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

autodoc_default_options = {
    "member-order": "bysource",
}

suppress_warnings = ["image.not_readable"]
