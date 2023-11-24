import os
import yaml
import sys
from pathlib import Path
from motbxtools import motbxschema

MOTBX_DIR = Path.cwd()


if __name__ == "__main__":
    version = sys.argv[2]
    print(version, sys.argv)
    if version == "latest":
        with open(MOTBX_DIR.joinpath("resources/MOTBX_version.yaml"), "r") as f:
            MOTBX_VERSION = yaml.safe_load(f)
            print(MOTBX_VERSION['latest'])

    print(MOTBX_DIR)
    with open(MOTBX_DIR.joinpath("resources/summary/test.txt"), "w") as f:
        print(MOTBX_DIR, file=f)
