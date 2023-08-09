# Resources and tools for the EATRIS Multi-omics Toolbox<!-- omit from toc -->

- [About](#about)
  - [EATRIS](#eatris)
  - [Multi-omics Toolbox (MOTBX)](#multi-omics-toolbox-motbx)
  - [This repository](#this-repository)
- [Use tools](#use-tools)
  - [Install Conda environment and Jupyter](#install-conda-environment-and-jupyter)
- [Contribute](#contribute)

## About

### EATRIS

[EATRIS](https://eatris.eu/) is the European infrastructure for translational medicine that brings together resources and services for research communities to translate scientific discoveries into benefits for patients. The organisation is a non-profit that provides access to a vast array of expertise and facilities from over 150 top-tier academic centres across Europe. EATRIS focuses on improving and optimising preclinical and early clinical development of drugs, vaccines and diagnostics, and overcome barriers to health innovation. Find out more here: https://eatris.eu/

### Multi-omics Toolbox (MOTBX)

The EATRIS [Multi-omics Toolbox (MOTBX)](<insert-link-to-motbx>) is a community-driven comprehensive knowledge base aimed at supporting researchers in academia and industry who are involved in the development, implementation, and adoption of multi-omics approaches for personalised medicine. MOTBX collects a rich selection of resources, including best practices, protocols for individual omics technologies, and tools for quality control and assessment. <MOTBX is available at insert-link.>

### This repository

This repository collects resources for MOTBX, a data model defing the structure of resources, and tools to maintain them.

| Folder / File | Description |
|--------------|-------------|
| **`notebooks/`** | Jupyter notebooks
| &emsp; `schema.ipynb` | Define JSON schema
| &emsp; `validate.ipynb` | Validate resource against JSON schema
| &emsp; `summarise.ipynb` | Create CSV file from multiple YAML resources
| &emsp; `ext_biotoolsAPI.ipynb` | Query bio.tools registry using API
| &emsp; `ext_FAIRsharingAPI.ipynb` | Query FAIRsharing registry using API
| **`resources/`** 
| &emsp; `curated/*.yaml` | Curated MOTBX resources
| &emsp; `external/*.yaml` | MOTBX resources from added from external databases
| **`schema/`**
| &emsp; `motbxschema.json` | JSON Schema defining MOTBX resource structure
| **`src/`** | Python modules
| **`test/`** | Files for testing (YAML, CSV)

## Use tools

A set of Jupyter notebooks provide functionality to create/modify the schema and validate resources.

### Install Conda environment and Jupyter

1. Install Miniconda3 (Conda 23.5.2 Python 3.11.3 released July 13, 2023)

2. Install *notebook* and Jupyter kernels (*nb_conda_kernels*) to Conda base environment
    ```
    conda install -c conda-forge notebook
    conda install -c conda-forge nb_conda_kernels
    ```

3. Create new environment and register kernel for Jupyter
    ```
    conda create -n motbxtools python=3.11 
    conda activate motbxtools
    conda install ipykernel
    python -m ipykernel install --user --name=motbxtools --display-name "Python 3.11 (motbxtools)"
    conda install -c anaconda requests
    conda install -c conda-forge pyyaml
    conda install -c conda-forge jsonschema
    conda install -c conda-forge validators
    ```

4. Run Jupyter notebook from base environment
    ```
    jupyter notebook
    ```

Alternatively, install environment from YAML file.
```
conda env create -f conda/environment.yml
```

## Contribute

<create-issue>

