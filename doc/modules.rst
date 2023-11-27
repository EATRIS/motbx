`motbxtools` Python package
===========================

The `motbxtools` package provides classes and methods to read, write, validate,
or summarise MOTBX resources. It is available in the directory `src/motbxtools`_.


Module `motbxschema`
--------------------

.. automodule:: motbxschema
    :members:
    :special-members: __init__


Unit testing
------------

The directory `tests/test_motbxtools`_ contains unit tests for the `motbxtools` package.
The `tests`_ directory additionally contains MOTBX resource `YAML` files used by the tests.
Unit tests can be run using the GitHub action defined in `.github/workflows/tests.yml`_ via `actions`_.
This action is triggered by changes to files in `src`_, `schema`_, or `tests`_.


.. _src/motbxtools: https://github.com/EATRIS/motbx/tree/main/src/motbxtools
.. _tests/test_motbxtools: https://github.com/EATRIS/motbx/tree/main/tests/test_motbxtools
.. _tests: https://github.com/EATRIS/motbx/tree/main/tests
.. _.github/workflows/tests.yml: https://github.com/EATRIS/motbx/blob/main/.github/workflows/tests.yml
.. _actions: https://github.com/EATRIS/motbx/actions/workflows/tests.yml
.. _src: https://github.com/EATRIS/motbx/tree/main/src
.. _schema: https://github.com/EATRIS/motbx/tree/main/schema