"""Validate MOTBX resources

This script validates MOTBX resources (YAML files).
"""
import argparse
from pathlib import Path
from motbxtools import motbxschema


MOTBX_DIR = Path.cwd()
# path to JSON SCHEMA file defining structure of MOTBX resources
SCHEMA_JSON = MOTBX_DIR.joinpath("schema/motbxschema.json")


parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument(
    'file_path',
    type=str,
    help="""File path to MOTBX resource YAML file.""")


def main(resource_path):
    print("Validating resource:", resource_path)
    assert resource_path.endswith(".yaml")
    # load MOTBX schema used for validation
    schema = motbxschema.MotbxSchema(SCHEMA_JSON)
    try:
        resource = motbxschema.MotbxResource(resource_path)
        print("Title:", resource.resource["resourceTitle"])
        print("URL:", resource.resource["resourceUrl"])
        # validate MOTBX resource
        resource.validate(schema)
        print("MOTBX resource passed validation.")
    except Exception as error:
        print("MOTBX resource is not valid.")
        print(error)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.file_path)
