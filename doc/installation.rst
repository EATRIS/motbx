Install `motbxtools` and use example notebooks
==============================================

Several Jupyter notebooks using the `motbxtools` Python library are provided as
part of the `MOTBX GitHub repository`_. We make use of `Conda`_ for cross-platform
package management.


Install Conda environment
-------------------------

1. Install `Miniconda3`_ (Conda 23.5.2 Python 3.11.3 released July 13, 2023).

2. Install dependencies

   A. Option 1: install environment from `YAML environment file`_ ::

         conda env create -f envs/motbxtools_notebooks.yml
         conda activate motbxtools_notebooks
         pip install -e .

   B. Option 2: install dependencies manually using Miniconda/Anaconda Prompt or terminal

      i. Install `notebook` and Jupyter kernels (`nb_conda_kernels`) to Conda base environment::

            conda install -c conda-forge notebook
            conda install -c conda-forge nb_conda_kernels

      ii. Create new environment and register kernel for Jupyter::

            conda create -n motbxtools_notebooks python=3.11
            conda activate motbxtools_notebooks
            conda install ipykernel
            python -m ipykernel install --user --name=motbxtools_notebooks --display-name "Python 3.11 (motbxtools_notebooks)"
            conda install -c anaconda requests
            conda install -c conda-forge pyyaml
            conda install -c conda-forge jsonschema
            conda install -c conda-forge validators
            conda install -c conda-forge pygithub
            conda install -c conda-forge keyring
            conda install -c anaconda pandas
            conda install -c conda-forge openpyxl
            pip install -e .


Run Jupyter
-----------

Jupyter can now be started from the base environment::

   jupyter notebook

This opens Jupyter in your default browser. Select a notebook from the
`notebooks`_ folder to open it.


Example Jupyter Notebooks
-------------------------

A set of `Jupyter notebooks`_ showcase how `motbxtools` can be used to create/modify
the MOTBX resource schema and validate resources.
Make sure to run them from the `notebooks`_ directory.


.. _MOTBX GitHub repository: https://github.com/EATRIS/motbx
.. _Conda: https://docs.conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/projects/miniconda/en/latest/
.. _YAML environment file: https://github.com/EATRIS/motbx/blob/main/envs/motbxtools_notebooks.yml
.. _notebooks: https://github.com/EATRIS/motbx/tree/main/notebooks
.. _Jupyter notebooks: https://github.com/EATRIS/motbx/tree/main/notebooks