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

Script `utils.validate_resource`
--------------------------------

.. argparse::
    :module: utils.validate_resource
    :func: parser
    :prog: validate_resource

This script can be executed as GitHub Action `validate_resources`_, which is
automatically triggered on pull requests when files in the `curated resources directory`_
are changed.


.. _motbxtools.utils: https://github.com/EATRIS/motbx/tree/main/src/motbxtools/utils
.. _create_summary: https://github.com/EATRIS/motbx/actions/workflows/create_summary.yml
.. _validate_resources: https://github.com/EATRIS/motbx/actions/workflows/validate_resources.yml
.. _curated resources directory: https://github.com/EATRIS/motbx/tree/main/resources/curated