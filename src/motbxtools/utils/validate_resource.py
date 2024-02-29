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
    print("\nValidating resource:", resource_path)
    try:
        print(resource_path)
        assert resource_path.endswith(".yaml")
    except AssertionError:
        print("Validation failed - MOTBX resources must be YAML files (.yaml)")
        print("resource_path:", resource_path)
        raise
    # load MOTBX schema used for validation
    schema = motbxschema.MotbxSchema(SCHEMA_JSON)
    try:
        resource = motbxschema.MotbxResource(resource_path)
    except Exception:
        print("Validation failed - resource could not be loaded")
        raise
    print("Title:", resource.resource["resourceTitle"])
    print("URL:", resource.resource["resourceUrl"])
    # validate MOTBX resource
    try:
        resource.validate(schema)
    except Exception:
        print("Validation failed - YAML file is not according to schema")
        raise
    print("MOTBX resource passed validation")
    print(79*"-", "\n")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.file_path)
