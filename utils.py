import json
from typing import Dict, Any

def read_file(filename: str) -> Dict[str, Any]:
    """
    Function which reads initial file and transforms it to dict.

    :param: str filename: input file
    :returns: read file as a dictionary from JSON file
    :rtype: Dict[str, Any]
    """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
