# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Mecrisp Ice'
copyright = """ `Mecrisp Ice
Documentation <https://mecrisp-ice.readthedocs.io>`__
by Christopher Lozinski and Matthias Koch is licensed under `CC BY-SA
4.0\ |image1|\ |image2|\ |image3| <https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1>`__

.. |image1| image:: https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1
.. |image2| image:: https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1
.. |image3| image:: https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1

"""


author = 'Chrisopher Lozinski'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
