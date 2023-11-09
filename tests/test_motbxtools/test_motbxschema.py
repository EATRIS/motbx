#! /usr/bin/env python
import unittest
import os
import jsonschema
import requests
import pathlib
from motbxtools import motbxschema

DATA_DIR = pathlib.Path(__file__).parents[1]
RESOURCES_PASS_DIR = DATA_DIR.joinpath("resources_pass")
RESOURCES_FAIL_DIR = DATA_DIR.joinpath("resources_fail")
SCHEMA_FILE = pathlib.Path(__file__).parents[2].joinpath(
    "schema/motbxschema.json")


class TestMotbxSchema(unittest.TestCase):
    """Test JSON schema that defines structure of MOTBX resources.
    """
    def test_validate(self):
        try:
            schema = motbxschema.MotbxSchema(SCHEMA_FILE)
            schema.validate()
        except Exception:
            self.fail("MotbxSchema() could not be instantiated/validated.")


class TestMotbxResourceMethods(unittest.TestCase):
    """Test that validation of MOTBX resources succeeds for given examples and
    fails under certain conditions.
    """
    def setUp(self):
        self.schema = motbxschema.MotbxSchema(SCHEMA_FILE)
        self.resources_pass = RESOURCES_PASS_DIR
        self.resources_fail = RESOURCES_FAIL_DIR

    def test_validate_pass(self):
        """Validation of these resources should succeed
        """
        # iterate through resources
        for root, dirs, files in os.walk(self.resources_pass):
            for name in files:
                if not name.endswith(".yaml"):
                    continue
                # load test resource and validate
                resource = motbxschema.MotbxResource(os.path.join(root, name))
                try:
                    resource.validate(self.schema)
                except Exception:
                    self.fail("MotbxResource.validate() failed")

    # def test_validate_failDate(self):
    #     """These MOTBX resources do not meet the requirements. Test that
    #     their validation fails.
    #     """
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         resource = motbxschema.MotbxResource(
    #             os.path.join(self.resources_fail, "testfailDate.yaml"))
    #         resource.validate(self.schema)

    def test_validate_failNoDesc(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailNoDesc.yaml"))
            resource.validate(self.schema)

    def test_validate_failUrl1(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailUrl1.yaml"))
            resource.validate(self.schema)

    def test_validate_failSubcategory(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailSubcategory.yaml"))
            resource.validate(self.schema)

    def test_validate_failUrl2(self):
        with self.assertRaises(AssertionError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailUrl2.yaml"))
            resource.validate(self.schema)

    def test_validate_failUrl3(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailUrl3.yaml"))
            resource.validate(self.schema)


if __name__ == '__main__':
    unittest.main()
