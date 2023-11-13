Build documentation
===================

This documentation was built using `Sphinx`_.

The following commands can be used to create a `Conda`_ environment that contains all packages needed to build the documentation.

1. Install `Miniconda3`_ (Conda 23.5.2 Python 3.11.3 released July 13, 2023)

2. Install dependencies

    A. Option 1: install dependencies manually using Miniconda/Anaconda Prompt or terminal::

            conda create -n motbxdoc python=3.11
            conda activate motbxdoc
            conda install -c conda-forge sphinx
            conda install -c conda-forge furo
            conda install -c conda-forge jsonschema
            conda install -c conda-forge validators
            conda install -c anaconda requests
            conda install -c conda-forge pyyaml
            pip install -e .


    B. Option 2: install environment from `YAML environment file`_ ::

            conda env create -f envs/motbxdoc.yml

The `HTML` documentation can be built using::

    make html

.. _Conda: https://docs.conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/projects/miniconda/en/latest/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _YAML environment file: https://github.com/EATRIS/motbx/blob/main/envs/motbxdoc.yml