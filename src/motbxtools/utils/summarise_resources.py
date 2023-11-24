"""Create a summary CSV file of MOTBX resources (YAML files).
"""
import os
import yaml
import sys
from pathlib import Path
from motbxtools import motbxschema

MOTBX_DIR = Path.cwd()
# file defining MOTBX resource summary version
VERSION_FILE = MOTBX_DIR.joinpath("resources/motbx_versions.yaml")
# path to JSON SCHEMA file defining structure of MOTBX resources
SCHEMA_JSON = MOTBX_DIR.joinpath("schema/motbxschema.json")
# path to directory where resources YAML file are saved
RESOURCES_DIR = MOTBX_DIR.joinpath("resources/curated")
# path to directory where summary files are saved
SUMMARY_DIR = MOTBX_DIR.joinpath("resources/summary")


if __name__ == "__main__":
    version = sys.argv[1]
    print("Received input 'version':", version)
    with open(VERSION_FILE, "r") as f:
        motbx_versions = yaml.safe_load(f)
    # get latest version based on input parameter 'version'
    if version == "latest":
        latest_version = motbx_versions["latest"]
        print("Updating latest version:", latest_version)
    else:
        with open(VERSION_FILE, "w") as f:
            motbx_versions["previous"].insert(0, motbx_versions["latest"])
            latest_version = motbx_versions["latest"] = version
            yaml.dump(motbx_versions, VERSION_FILE)
            print("Creating new version:", latest_version)
    # get previous version
    previous_version = motbx_versions["previous"][0]
    print("Comparing to previous version:", previous_version)

    # define file paths
    summary_csv_previous_fp = SUMMARY_DIR.joinpath(
        f"MOTBX_{previous_version}.csv")
    # these files will be created or overwritten
    summary_csv_latest_fp = SUMMARY_DIR.joinpath(
        f"MOTBX_{latest_version}.csv")
    summary_csv_latest_excl_invalid_fp = SUMMARY_DIR.joinpath(
        f"MOTBX_{latest_version}_excl_invalid.csv")
    changelog_csv_fp = SUMMARY_DIR.joinpath(
        f"changelog_{latest_version}.csv")
    validation_report_fp = SUMMARY_DIR.joinpath(
        f"validation_report_{latest_version}.txt")

    # create a MotbxCollection object
    motbx_collection = motbxschema.MotbxCollection(RESOURCES_DIR, SCHEMA_JSON)
    # validate resources and create summary CSV file; keep invalid resources
    motbx_collection.summarise(
        summary_csv_latest_fp,
        validate=True,
        exclude_invalid=False,
        old_summary_csv_path=summary_csv_previous_fp,
        changelog_path=changelog_csv_fp,
        validationlog_path=validation_report_fp)
    # validate resources and create summary CSV file; exclude invalid resources
    motbx_collection.summarise(
        summary_csv_latest_excl_invalid_fp,
        validate=True,
        exclude_invalid=True,
        old_summary_csv_path=summary_csv_previous_fp)
