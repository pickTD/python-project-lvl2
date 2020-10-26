"""Generate diff."""
import json
from itertools import chain
from os import path


def get_result_string(key, first_value='', second_value='', sign=''):
    """Сreates a line showing the difference.

    Args:
        sign (str): Graphical representation of changes.
        key (str): Сompare key.
        first_value (str): Сompare key value.
        second_value (str): Сompare key value (to display changes).

    Returns:
        str: Line showing the difference.
    """
    if not second_value:
        return '  {0} {1}: {2}'.format(sign, key, first_value)
    return '  - {0}: {1}\n  + {2}: {3}'.format(
        key, first_value, key, second_value,
    )


def parse_json(file_path):
    """Parse json file.

    Args:
        file_path (Path): Path to json file.

    Returns:
        str: Parsed json.
    """
    with open(path.abspath(file_path)) as json_file:
        return json.load(json_file)


def generate_diff(first_file, second_file):  # noqa: WPS210
    """Generate diff between two files.

    Args:
        first_file (str): Plain json file for comparison.
        second_file (str): Plain json file for comparison.

    Returns:
        str: Difference between two files.
    """
    first_json = parse_json(first_file)
    second_json = parse_json(second_file)
    first_keys = set(first_json)
    second_keys = set(second_json)

    unchanged_keys = set(filter(
        lambda key: first_json[key] == second_json[key],
        first_keys & second_keys,
    ))

    unchanged = map(
        lambda key: get_result_string(key, first_json[key], sign=' '),
        unchanged_keys,
    )
    removed = map(
        lambda key: get_result_string(key, first_json[key], sign='-'),
        first_keys - second_keys,
    )
    added = map(
        lambda key: get_result_string(key, second_json[key], sign='+'),
        second_keys - first_keys,
    )
    changed = map(
        lambda key: get_result_string(key, first_json[key], second_json[key]),
        first_keys & second_keys - unchanged_keys,
    )

    diff = (list(chain(unchanged, removed, added, changed)))

    return '\n'.join(['{', *diff, '}'])
