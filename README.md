# Resources and tools for the EATRIS Multi-omics Toolbox<!-- omit from toc -->

- [EATRIS](#eatris)
- [Multi-omics Toolbox (MOTBX)](#multi-omics-toolbox-motbx)
- [This repository](#this-repository)
  - [Contribute to MOTBX](#contribute-to-motbx)
  - [Structure of this repository](#structure-of-this-repository)
  - [Development](#development)
  - [Running notebooks](#running-notebooks)
- [Acknowledgements](#acknowledgements)

## EATRIS

[<img src="https://github.com/EATRIS/.github/assets/1405356/06fb628b-13b9-4a9b-aef3-a4987d989bf6" alt="EATRIS logo" width="200"/>](https://eatris.eu/)

EATRIS is the [European infrastructure for translational medicine](https://eatris.eu/) that brings together resources and services for research communities to translate scientific discoveries into benefits for patients. The organisation is a non-profit that provides access to a vast array of expertise and facilities from over 150 top-tier academic centres across Europe. EATRIS focuses on improving and optimising preclinical and early clinical development of drugs, vaccines and diagnostics, and overcome barriers to health innovation. Find out more here: https://eatris.eu/

## Multi-omics Toolbox (MOTBX)

[<img src="https://github.com/EATRIS/motbx/assets/1405356/3973fe3c-27b7-410a-80ae-7bf0a2927e8c" alt="MOTBX logo" width="200"/>](https://motbx.eatris.eu/)

The EATRIS [Multi-omics Toolbox (MOTBX)](https://motbx.eatris.eu/) is a community-driven comprehensive knowledge base aimed at supporting researchers in academia and industry who are involved in the development, implementation, and adoption of multi-omics approaches for personalised medicine. MOTBX collects a rich selection of resources, including best practices, protocols for individual omics technologies, and tools for quality control and assessment. MOTBX is available at https://motbx.eatris.eu/.

## This repository

[This repository](https://github.com/EATRIS/motbx) collects resources for MOTBX, a data model defing the structure of resources, and tools to maintain them.

### Contribute to MOTBX

The EATRIS Multi-omics Toolbox is a community effort and suggestions for new resources are very welcome. You can [submit an issue](https://github.com/EATRIS/motbx/issues/new/choose) to request addition of a new resource, changes to existing resources, or removal of a resource. We also welcome new ideas for this repository, or developers who want to actively contribute to it. [Contact us](https://motbx.eatris.eu/contact/) if you have any questions.

### Structure of this repository

| Folder / File | Description |
|--------------|-------------|
| [**`.github/`**](https://github.com/EATRIS/motbx/tree/main/.github) | [Issue templates](https://github.com/EATRIS/motbx/tree/main/.github/ISSUE_TEMPLATE) and [GitHub actions](https://github.com/EATRIS/motbx/tree/main/.github/workflows)
| [**`envs/motbxtools.yml`**](https://github.com/EATRIS/motbx/blob/main/envs/motbxtools.yml) | [Conda](https://conda.io/) environment file specifying dependencies
| [**`notebooks/`**](https://github.com/EATRIS/motbx/tree/main/notebooks) | Jupyter notebooks - make sure to run them from the `notebooks` directory
| &emsp; [`schema.ipynb`](https://github.com/EATRIS/motbx/blob/main/notebooks/schema.ipynb) | This notebook was used to create the JSON schema file [`motbxschema.json`](https://github.com/EATRIS/motbx/blob/main/schema/motbxschema.json)
| &emsp; [`add_legacy_resources.ipynb`](https://github.com/EATRIS/motbx/blob/main/notebooks/add_legacy_resources.ipynb) | A first version of MOTBX resources was added based on information collected in an Excel file (`resources\legacy\MOTBX_resources_for_website - Copy 2023-07-28.xlsx`). Each row was converted to YAML files using the Jupyter notebook `notebooks\add_legacy_resources.ipynb`. This first version allows resource URLs deviating from the pattern `https://*` and additionaly allowing `http://*`, `ftp://`, and `*.pdf`.
| &emsp; [`validate.ipynb`](https://github.com/EATRIS/motbx/blob/main/notebooks/validate.ipynb) | This notebook can be used to validate [all resources](https://github.com/EATRIS/motbx/tree/main/resources/curated) against the [JSON schema](https://github.com/EATRIS/motbx/blob/main/schema/motbxschema.json)
| &emsp; [`summarise.ipynb`](https://github.com/EATRIS/motbx/blob/main/notebooks/summarise.ipynb) | Create CSV file from [all resources](https://github.com/EATRIS/motbx/tree/main/resources/curated) - each YAML file as one row in the CSV file
| &emsp; `ext_biotoolsAPI.ipynb` | Query bio.tools registry using API
| &emsp; `ext_FAIRsharingAPI.ipynb` | Query FAIRsharing registry using API
| [**`resources/curated/*.yaml`**](https://github.com/EATRIS/motbx/tree/main/resources/curated) | Curated MOTBX resources in YAML format
| [**`schema/motbxschema.json`**](https://github.com/EATRIS/motbx/blob/main/schema/motbxschema.json) | JSON Schema defining MOTBX resource structure
| [**`src/motbxtools`**](https://github.com/EATRIS/motbx/tree/main/src/motbxtools) | Python module with classes for MOTBX resources and MOTBX resource schema including functions for resource validation
| [**`test/`**](https://github.com/EATRIS/motbx/tree/main/tests) | Files for testing (YAML, CSV) and [Python module](https://github.com/EATRIS/motbx/tree/main/tests/test_motbxtools) for testing [`src/motbxtools`](https://github.com/EATRIS/motbx/tree/main/src/motbxtools)

### Development

When making changes to this repository, we follow the [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow).

### Running notebooks

A set of [Jupyter notebooks](https://github.com/EATRIS/motbx/tree/main/notebooks) provide functionality to create/modify the MOTBX resource schema and validate resources. We provide a conda environment file to install dependencies for running the notebooks locally.



## Acknowledgements

The first version of MOTBX was developed by the flagship project [EATRIS-Plus](https://eatris.eu/projects/eatris-plus/) and EATRIS. We thank everyone for their valuable contributions!

<List of contributors>

* [Name]("https://orcid.org/"), Affiliation
* [Name]("https://orcid.org/"), Affiliation
