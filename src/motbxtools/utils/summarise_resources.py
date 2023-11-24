import os
import yaml
from pathlib import Path
from motbxtools import motbxschema

MOTBX_DIR = Path.cwd()


if __name__ == "__main__":
    print(MOTBX_DIR)
    with open(MOTBX_DIR.joinpath("resources/summary/test.txt"), "w") as f:
        print(MOTBX_DIR, file=f)
