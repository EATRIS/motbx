Scripts and GitHub Actions
==========================

Scripts for executing specific tasks are available in the `motbxtools.utils`_
module. They can be run locally, or as automated GitHub Actions.

Script `utils.summarise_resources`
----------------------------------

.. argparse::
    :module: utils.summarise_resources
    :func: parser
    :prog: summarise_resources

This script can be executed as GitHub Action `create_summary`_.

.. _motbxtools.utils: https://github.com/EATRIS/motbx/tree/main/src/motbxtools/utils
.. _create_summary: https://github.com/EATRIS/motbx/actions/workflows/create_summary.yml