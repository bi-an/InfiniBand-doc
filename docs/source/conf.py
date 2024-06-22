# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Chinese Search Support
import os
import jieba

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'InfiniBand Learning'
copyright = '2024, bi-an'
author = 'bi-an'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe',
    'recommonmark',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# The following two lines confige jiaba to support the Chinese Search
# https://blog.51cto.com/u_16175517/6935688
html_search_language = 'zh'
html_search_options = {
    'dict': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dict.txt')
}

def setup(app):
    app.add_css_file('custom.css')
