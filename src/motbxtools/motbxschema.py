"""This module contains classes for the Multi-omics Toolbox (MOTBX) JSON
schema, the MOTBX resource (single YAML file), and the MOTBX collection (all
YAML files in a directory that describe resources).
"""
import csv
import json
import jsonschema
import os
import requests
import sys
import validators
import yaml
from contextlib import contextmanager


class MotbxSchema():
    """This class stores a JSON Schema as a dictionary.
    """
    def __init__(self, json_path):
        assert str(json_path).endswith(".json")
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
    def __init__(self, yaml_path, resource=None):
        """Initialise MOTBX resource object.

        :param yaml_path: Path to YAML file containing a MOTBX resource
        :type yaml_path: str
        :param resource: A MOTBX resource
        :type resource: dict
        """
        assert str(yaml_path).endswith((".yml", ".yaml"))
        self._yaml_path = yaml_path
        self.resource = resource
        try:
            self.load()
        except FileNotFoundError:
            assert self.resource is not None
        return

    def load(self):
        """Load a MOTBX resource from a YAML file.
        """
        with open(self._yaml_path, "r") as fp:
            assert self.resource is None
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

        :param motbx_schema: A JSON schema defining structure of MOTBX resource
        :type motbx_schema: :class:`~MotbxSchema`
        :raises Exception: Validation of URL fails
        """
        assert isinstance(motbx_schema, MotbxSchema)
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
    """This class collects all MOTBX resources in a directory.
    """
    def __init__(self, collection_dir, schema_json_path):
        """Initialise MOTBX collection object.

        :param collection_dir: Path to directory containing MOTBX resources
        :type collection_dir: str
        """
        assert os.path.isdir(collection_dir)
        assert str(schema_json_path).endswith(".json")
        self._collection_dir = collection_dir
        self.schema = MotbxSchema(schema_json_path)
        self.schema.validate()
        self.fieldnames = list(self.schema.schema["properties"].keys())
        return

    def get_info(self, fields=None):
        """Retrieve information about values present in given field(s) for
        MOTBX resources in directory.

        :param fields: List with field names or tuples of fieldnames to
            retrieve
        :type fields: list
        """
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
                    except KeyError:  # k is tuple
                        v = tuple([resource.resource[i] for i in k])
                    if isinstance(v, str) or isinstance(v, tuple):
                        info[k].add(v)
                    else:
                        info[k] |= set(v)
        return info

    @contextmanager
    def _validation_file(self, file_path=None):
        """Create text file for collecting information on failed resource
        validations.

        :param file_path: Path to a validation log CSV file
        :type file_path: str
        """
        if not file_path:
            yield None
        else:
            assert str(file_path).endswith(".txt")
            vf = open(file_path, "w", newline="", encoding="utf-8")
            print("VALIDATION REPORT - MOTBX resources that failed validation",
                  file=vf)
            print(79*"=", file=vf)
            try:
                yield vf
            finally:
                vf.close()

    @contextmanager
    def _summary_file(self, file_path):
        """Create CSV file summarising MOTBX resources.

        :param file_path: Path to a MOTBX summary CSV file
        :type file_path: str
        """
        assert str(file_path).endswith(".csv")
        sf = open(file_path, "w", newline="", encoding="utf-8")
        summary = csv.DictWriter(sf, fieldnames=self.fieldnames)
        summary.writeheader()
        try:
            yield summary
        finally:
            sf.close()

    @contextmanager
    def _changelog_file(self, file_path=None):
        """Create CSV file summarising changes in MOTBX resources comparing two
        versions of MOTBX

        :param file_path: Path to a MOTBX summary CSV file
        :type file_path: str
        """
        if not file_path:
            yield None
        else:
            assert str(file_path).endswith(".csv")
            cf = open(file_path, "w", newline="", encoding="utf-8")
            changelog = csv.DictWriter(cf, fieldnames=[
                "resourceID", "Resource status [added/updated/removed]",
                "Passed validation [yes/no]", "Updated field(s)"])
            changelog.writeheader()
            try:
                yield changelog
            finally:
                cf.close()

    def _load_summary(self, file_path):
        """Load a MOTBX summary CSV file.

        :param file_path: Path to a MOTBX summary CSV file
        :type file_path: str
        """
        assert str(file_path).endswith(".csv")
        summary = {}
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                summary[row["resourceID"]] = row
        return summary

    def summarise(self, summary_csv_path, validate=True, exclude_invalid=False,
                  old_summary_csv_path=None, changelog_path=None,
                  validationlog_path=None, verbose=True):
        """Summarise all MOTBX resources in folder and write to CSV file.

        :param summary_csv_path: Path to CSV file summarising resources of
            latest MOTBX version
        :type summary_csv_path: str
        :param validate: Validate resource against JSON schema if True
        :type validate: bool
        :param verbose: Print processed resource IDs if True
        :type verbose: bool
        :param old_summary_csv_path: Path to CSV file summarising resources of
            previous MOTBX version
        :type old_summary_csv_path: str
        :param changelog_path: Path to CSV file summarising changes
        :type changelog_path: str
        :param validationlog_path: Path to CSV file summarising failed
            validations
        :type validationlog_path: str
        """
        if old_summary_csv_path:  # load summary CSV from previous version
            summary_old = self._load_summary(old_summary_csv_path)

        with (self._summary_file(summary_csv_path) as summary,
              self._changelog_file(changelog_path) as changelog,
              self._validation_file(validationlog_path) as errorlog):
            if not errorlog:
                errorlog = sys.stdout

            resource_ids = set()
            # iterate through resources
            for root, dirs, files in os.walk(self._collection_dir):
                for name in files:
                    if not name.endswith(".yaml"):
                        continue
                    if verbose:
                        print("Loading MOTBX resources |", name, end="\r")

                    # load one MOTBX resource
                    resource = MotbxResource(os.path.join(root, name))
                    invalid = False
                    if validate:  # validate against JSON schema
                        try:
                            resource.validate(self.schema)
                        except Exception as error:
                            invalid = True
                            # print validation errors to validation report file
                            print(error, file=errorlog)
                            print("Resource:", name, file=errorlog)
                            print("URL:", resource.resource["resourceUrl"],
                                  file=errorlog)
                            print(79*"-", file=errorlog)

                    if exclude_invalid and invalid:
                        continue
                    # write resource to summary CSV file
                    row = resource.flatten(self.fieldnames)
                    summary.writerow(row)
                    resource_ids.add(row["resourceID"])

                    # compare to older version
                    if old_summary_csv_path:
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
                            if len(changed_fields) > 0:  # else no changes
                                change_row = {
                                    "resourceID": row["resourceID"],
                                    "Resource status [added/updated/removed]":
                                    "added" if new_resource else "updated",
                                    "Updated field(s)":
                                    ", ".join(changed_fields)}
                                if validate:
                                    change_row["Passed validation [yes/no]"
                                               ] = "no" if invalid else "yes"
                                changelog.writerow(change_row)

            # check which resources have been removed
            if old_summary_csv_path and changelog_path:
                removed_ids = [k for k in summary_old.keys()
                               if k not in resource_ids]
                for i in removed_ids:
                    changelog.writerow({
                        "resourceID": i,
                        "Resource status [added/updated/removed]": "removed"})

        return
