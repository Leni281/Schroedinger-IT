"""
Configuration file for the Sphinx documentation builder.

This file contains configuration settings for Sphinx, a documentation generation tool.
It specifies project information, extensions, and other options for generating documentation.
"""
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

PROJECT = 'Schroedinger Equation'
CUSTOM_COPYRIGHT = '2023, Oksana Bunk, Alenica Heußner'
AUTHOR = 'Oksana Bunk, Alenica Heußner'

# The full version, including alpha/beta/rc tags
RELEASE = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
HTML_THEME = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
