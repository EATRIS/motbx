MOTBX resources and schema
==========================

MOTBX resources are stored as `YAML` files. The `YAML` file structure is defined
using `JSON Schema`.

Curated MOTBX resources are stored in the `resources/curated`_ directory, the `JSON Schema` is
available under `schema/motbxschema.json`_. It defines the mandatory (`resourceID`,
`resourceCategory`, `resourceSubcategory`, `resourceTitle`, `resourceDescription`, `resourceUrl`, `resourceTags`)
and optional (`resourceKeywords`) fields describing a MOTBX resource, allowed values
for `resourceCategory` and `resourceSubcategory`, and allowed patterns for `resourceUrl`.

The `JSON Schema` file `schema/motbxschema.json`_ was created with the Jupyter notebook `notebooks/schema.ipynb`_.


.. _resources/curated: https://github.com/EATRIS/motbx/tree/main/resources/curated
.. _schema/motbxschema.json: https://github.com/EATRIS/motbx/blob/main/schema/motbxschema.json
.. _notebooks/schema.ipynb: https://github.com/EATRIS/motbx/blob/main/notebooks/schema.ipynb