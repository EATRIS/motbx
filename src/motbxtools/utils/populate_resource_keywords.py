"""Add resourceKeywords to MOTBX resources

This script adds resourceKeywords to MOTBX resources (YAML files) based on
existing resourceTags.
"""
import argparse
import yaml
from collections import defaultdict as ddict
from pathlib import Path
from motbxtools import motbxschema


MOTBX_DIR = Path.cwd()
# path to JSON SCHEMA file defining structure of MOTBX resources
SCHEMA_JSON = MOTBX_DIR.joinpath("schema/motbxschema.json")
TAGS_KEYWORDS = MOTBX_DIR.joinpath("schema/tags_keywords.yaml")


parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument(
    'file_path',
    type=str,
    help="""File path to MOTBX resource YAML file.""")


def unnest(nested, pre=None):
    """Recursive function to unnest a nested object consisting of lists and
    dictionaries.
    """
    pre = pre[:] if pre else []
    if isinstance(nested, dict):
        for key, value in nested.items():
            if isinstance(value, dict):
                for d in unnest(value, pre + [key]):
                    yield d
            elif isinstance(value, list):
                for v in value:
                    for d in unnest(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    elif isinstance(nested, list):
        for value in nested:
            if isinstance(value, dict):
                for d in unnest(value, pre):
                    yield d
            elif isinstance(value, list):
                for v in value:
                    for d in unnest(v, pre):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [nested]


def get_tag_mapping(tag_mapping_yaml):
    """Create a tags-to-keywords mapping dictionary.

    :param tag_mapping_yaml: List of lists with tags and keywords
    :type tag_mapping_yaml: list
    :return: Mapping dictionary
    :rtype: dict
    """
    term2parents = ddict(set)
    term2synonyms = ddict(set)
    for mapl in unnest(tag_mapping_yaml):
        if "synonyms" in mapl:
            term2synonyms[mapl[-3]].add(mapl[-1])
        for idx, i in enumerate(mapl):
            if i == "synonyms":
                continue
            term2parents[i] |= set(mapl[:idx]) - set(["synonyms"])

    term2keywords = ddict(set)
    for k, v in term2parents.items():
        k = k.replace(" (tag)", "")
        v = set([i.replace(" (tag)", "") for i in v])
        term2keywords[k] |= v.union(*[term2synonyms[i] for i in v])

    return term2keywords


def main(resource_path):
    try:
        assert resource_path.endswith(".yaml")
    except AssertionError:
        print("AssertionError - MOTBX resources must be YAML files (.yaml)")
        print("resource_path:", resource_path)
    # load MOTBX schema used for validation
    resource = motbxschema.MotbxResource(resource_path)
    with open(TAGS_KEYWORDS, "r") as file:
        tag_mapping = get_tag_mapping(yaml.safe_load(file))
    try:
        resource_keywords = set(resource.resource["resourceKeywords"])
    except KeyError:
        resource_keywords = set()
    for tag in resource.resource["resourceTags"]:
        resource_keywords |= tag_mapping[tag]
    resource.resource["resourceKeywords"] = sorted(list(resource_keywords))
    resource.save()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.file_path)
