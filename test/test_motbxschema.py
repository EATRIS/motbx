#! /usr/bin/env python
import unittest
import os
import sys
module_path = os.path.abspath(os.path.join("src"))
if module_path not in sys.path:
    sys.path.append(module_path)
from motbxtools import motbxschema
import jsonschema
import requests


class TestMotbxSchema(unittest.TestCase):
    """Test JSON schema that defines structure of MOTBX resources.
    """    
    def test_validate(self):
        try:
            schema = motbxschema.MotbxSchema("schema/motbxschema.json")
            schema.validate()
        except:
            self.fail("MotbxSchema() could not be instantiated/validated.")


class TestMotbxResourceMethods(unittest.TestCase):
    """Test that validation of MOTBX resources succeeds for given examples and
    fails under certain conditions.
    """    
    def setUp(self):
        self.schema = motbxschema.MotbxSchema("schema/motbxschema.json")
        self.resources_pass = "test/resources_pass"
        self.resources_fail = "test/resources_fail"

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
                except:
                    self.fail("MotbxResource.validate() failed")
        
    def test_validate_fail(self):
        """These MOTBX resources do not meet the requirements. Test that their
        validation fails.
        """        
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailDate.yaml"))
            resource.validate(self.schema)

        with self.assertRaises(jsonschema.exceptions.ValidationError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailNoDesc.yaml"))
            resource.validate(self.schema)

        with self.assertRaises(requests.exceptions.ConnectionError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailUrl1.yaml"))
            resource.validate(self.schema)

        with self.assertRaises(requests.exceptions.HTTPError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailUrl2.yaml"))
            resource.validate(self.schema)

        with self.assertRaises(jsonschema.exceptions.ValidationError):
            resource = motbxschema.MotbxResource(
                os.path.join(self.resources_fail, "testfailUrl3.yaml"))
            resource.validate(self.schema)
        

if __name__ == '__main__':
    unittest.main()