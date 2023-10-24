#! /usr/bin/env python
import json
import jsonschema
import yaml
import requests
import validators


class MotbxSchema():
    """This class stores a JSON Schema as a dictionary.
    """
    def __init__(self, json_path):
        self._json_path = json_path
        with open(self._json_path, "r") as fp:
            self.schema = json.load(fp)
        self.validate()
        return

    def validate(self):
        """Validate schema against metaschema JSON schema draft 2020-12.
        """
        jsonschema.Draft202012Validator.check_schema(self.schema)
        return


class MotbxResource():
    """This class stores a MOTBX resource as a dictionary.
    """
    def __init__(self, yaml_path):
        """Initialise MOTBX resource object.

        :param yaml_path: Path to YAML file containing a MOTBX resource
        :type yaml_path: str
        """
        self._yaml_path = yaml_path
        self.load()
        return

    def load(self):
        """Load a MOTBX resource from a YAML file.
        """
        with open(self._yaml_path, "r") as fp:
            self.resource = yaml.safe_load(fp)
        return

    def validate(self, motbx_schema):
        """Validate MOTBX resource with JSON schema and confirm that URL is
        valid and live.

        :param motbx_schema: _description_
        :type motbx_schema: :class:`~MotbxSchema`
        :raises Exception: Validation of URL fails
        """
        # validate against JSON schema
        jsonschema.validate(
            self.resource, motbx_schema.schema,
            format_checker=jsonschema.FormatChecker())
        # validate URL (pattern https://* already validated by jsonschema)
        url = self.resource["resourceUrl"]
        if url.startswith("http"):
            try:
                response = validators.url(url, public=True)
                if not response:
                    raise Exception
            except Exception:
                raise
            # check if URL is live
            try:
                response = requests.get(url)
                if response.status_code not in (200, 403):
                    raise Exception
            except Exception:
                raise
        return

    def flatten(self, fieldnames):
        """Iterate through nested dictionary (from JSON) and return dictionary
        with single level for writing CSV file. Keep only keys present in
        fieldnames.

        :param fieldnames: CSV column names (fieldnames) of a
            :class:`~csv.DictWriter` instance
        :type fieldnames: list
        :return: A row for :func:`~csv.DictWriter.writerow`
        :rtype: dict
        """
        def _flatten(resource, fieldnames, row={}):
            """Recursive function to retrieve all required fields provided in
            fieldnames from the (nested) resource dictionary.

            :param resource: MOTBX resource or part of the resource
            :type resource: dict
            :param fieldnames: CSV column names (fieldnames) of a
                :class:`~csv.DictWriter` instance
            :type fieldnames: list
            :param row: An incomplete row for :func:`~csv.DictWriter.writerow`,
                defaults to {}
            :type row: dict, optional
            """
            for k, v in resource.items():
                if isinstance(v, str) and k in fieldnames:
                    row[k] = v
                elif isinstance(v, list) and k in fieldnames:
                    row[k] = ", ".join(v)
                elif isinstance(v, dict):
                    _flatten(v, fieldnames, row=row)
            return row

        row = _flatten(self.resource, fieldnames)
        return row
