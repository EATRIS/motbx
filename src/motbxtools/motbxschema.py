#! /usr/bin/env python
import csv
import json
import jsonschema
import os
import requests
import validators
import yaml
from motbxtools import utils


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

    def save(self):
        """Save the MOTBX resource to a YAML file.
        """
        with open(self._yaml_path, "w") as fp:
            yaml.dump(self.resource, fp)
        return

    def validate(self, motbx_schema):
        """Validate MOTBX resource with JSON schema and confirm that URL is
        valid and live.

        :param motbx_schema: _description_
        :type motbx_schema: :class:`~MotbxSchema`
        :raises Exception: Validation of URL fails
        """
        try:
            # validate against JSON schema
            # this includes checking URL for pattern https://* or *.pdf
            jsonschema.validate(
                self.resource, motbx_schema.schema,
                format_checker=jsonschema.FormatChecker())
        except jsonschema.exceptions.ValidationError:
            raise
        url = self.resource["resourceUrl"]
        try:
            # validate URL
            response = validators.url(url, public=True)
            # possible errors include SSLError
            assert response
        except Exception:
            raise
        try:
            # check if URL is live
            response = requests.get(url, timeout=10)
            assert response.status_code != 404
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


class MotbxCollection():
    """This class collects all MOTBX resources.
    """
    def __init__(self, collection_dir, schema_json_path):
        """Initialise MOTBX collection object.

        :param collection_dir: Path to directory containing MOTBX resources
        :type collection_dir: str
        """
        self._collection_dir = collection_dir
        self.schema = MotbxSchema(schema_json_path)
        self.schema.validate()
        self.fieldnames = list(self.schema.schema["properties"].keys())
        return

    def get_info(self, fields=None):
        if not fields:
            fields = [("resourceCategory", "resourceSubcategory"),
                      "resourceTags"]
        info = {k: set() for k in fields}
        # iterate through resources
        for root, dirs, files in os.walk(self._collection_dir):
            for name in files:
                if not name.endswith(".yaml"):
                    continue
                # load one MOTBX resource
                resource = MotbxResource(os.path.join(root, name))
                for k in fields:
                    try:
                        v = resource.resource[k]
                    except KeyError:
                        v = tuple([resource.resource[i] for i in k])
                    if isinstance(v, str) or isinstance(v, tuple):
                        info[k].add(v)
                    else:
                        info[k] |= set(v)
        return info

    def summarise(self, summary_csv_path, validate=True, verbose=True,
                  summary_csv_path_old=None, changelog_path=None):
        """Summarise all MOTBX resources in folder and write to CSV file

        :param summary_csv_path: Path to CSV file summarising resources of
            latest MOTBX version
        :type summary_csv_path: str
        :param validate: Validate resource against JSON schema if True
        :type validate: bool
        :param verbose: Print processed resource IDs if True
        :type verbose: bool
        :param summary_csv_path_old: Path to CSV file summarising resources of
            previous MOTBX version
        :type summary_csv_path_old: str
        :param changelog_path: Path to CSV file summarising changes
        :type changelog_path: str
        """
        if summary_csv_path_old:  # load summary CSV from previous version
            summary_old = {}
            with open(summary_csv_path_old, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if verbose:
                        print("Loading summary of previous MOTBX version  |",
                              row["resourceID"], end="\r")
                    summary_old[row["resourceID"]] = row

        with (open(summary_csv_path, "w", newline="", encoding="utf-8") as sf,
              utils.open_conditional(
                  changelog_path, "w", newline="", encoding="utf-8") as cf):
            if verbose and summary_csv_path_old:
                print()
            # create CSV writer for summary file
            summary = csv.DictWriter(sf, fieldnames=self.fieldnames)
            summary.writeheader()
            if changelog_path:  # create CSV writer for changelog
                changelog = csv.DictWriter(cf, fieldnames=[
                    "resourceID", "New resource (yes/no)", "Updated field(s)"])
                changelog.writeheader()

            # iterate through resources
            for root, dirs, files in os.walk(self._collection_dir):
                for name in files:
                    if not name.endswith(".yaml"):
                        continue
                    if verbose:
                        print("Loading resources for latest MOTBX version |",
                              name, end="\r")
                    # load one MOTBX resource
                    resource = MotbxResource(os.path.join(root, name))
                    if validate:  # validate against JSON schema
                        resource.validate(self.schema)
                    # write to CSV file
                    row = resource.flatten(self.fieldnames)
                    # write resource to summary file
                    summary.writerow(row)
                    if summary_csv_path_old:
                        new_resource = False
                        try:  # get resource from previous version using ID
                            row_old = summary_old[row["resourceID"]]
                        except KeyError:  # resource is new
                            row_old = {}
                            new_resource = True
                        if changelog_path:  # write changes to changelog
                            # determine which MOTBX resource fields differ
                            # between previous and latest version
                            changed_fields = sorted(dict(
                                set(row.items()) ^ set(row_old.items())
                                ).keys())
                            if len(changed_fields) > 0:
                                changelog.writerow({
                                    "resourceID": row["resourceID"],
                                    "New resource (yes/no)": "yes"
                                    if new_resource else "no",
                                    "Updated field(s)":
                                    ", ".join(changed_fields)
                                })
        return
