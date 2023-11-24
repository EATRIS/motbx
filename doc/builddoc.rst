Build documentation
===================

This `documentation`_ was built using `Sphinx`_.


Build locally
-------------

The following commands can be used to create a `Conda`_ environment that contains all packages needed to build the documentation.

1. Install `Miniconda3`_ (Conda 23.5.2 Python 3.11.3 released July 13, 2023)

2. Install dependencies

   A. Option 1: install environment from `YAML environment file`_ ::

         conda env create -f envs/motbxtools_doc.yml
         conda activate motbxtools_doc
         pip install -e .

   B. Option 2: install dependencies manually using Miniconda/Anaconda Prompt or terminal::

         conda create -n motbxtools_doc python=3.11
         conda activate motbxtools_doc
         conda install -c conda-forge furo
         conda install -c conda-forge jsonschema
         conda install -c conda-forge validators
         conda install -c anaconda requests
         conda install -c conda-forge pyyaml
         conda install -c conda-forge sphinx
         conda install -c conda-forge sphinx-argparse
         pip install -e .


The `HTML` documentation can be built using::

    make html


Deploy on GitHub pages
----------------------

A GitHub action has been defined to build the documention and deploy it on GitHub pages.
The action is defined in `.github/workflows/documentation.yml`_ and can be manually triggered via `actions`_.


.. _documentation: https://eatris.github.io/motbx/index.html
.. _Conda: https://docs.conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/projects/miniconda/en/latest/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _YAML environment file: https://github.com/EATRIS/motbx/blob/main/envs/motbxtools_doc.yml
.. _.github/workflows/documentation.yml: https://github.com/EATRIS/motbx/blob/main/.github/workflows/documentation.yml
.. _actions: https://github.com/EATRIS/motbx/actions/workflows/documentation.yml