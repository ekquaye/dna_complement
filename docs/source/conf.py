# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python dna_comp Package'
copyright = '2024, Max Planck Institute for Evolutionary Biology'
author = 'Max Planck'
version = "version = "0.0.1""

import sys

sys.path.insert(0, '../../dna_comp')

import dna_comp

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx_rtd_theme',
              'myst_parser',
              'sphinx.ext.napoleon',
              ]

dna_comps_path = ['_dna_comps']
exclude_patterns = []

source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
