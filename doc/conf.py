# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'JOLux'
copyright = 'Federal Chancellery'
author = 'Jean-Louis Morard, Benedikt Hitz-Gamper'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinxcontrib.mermaid']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# MyST configuration
myst_enable_extensions = [
    "colon_fence",
    "html_image",
]

# Mermaid configuration (optional, for specifying version)
mermaid_version = '8.11.0'  # Specify the version you want to use
mermaid_js_path = 'https://cdn.jsdelivr.net/npm/mermaid@8.11.0/dist/mermaid.min.js'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# add custom js for sparql link generation
def setup(app):
    app.add_js_file('sparql_link.js')
    app.add_css_file('custom.css')