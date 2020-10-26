#!/usr/bin/env python3
"""Gendiff."""
import click

from gendiff import generate_diff

context_settings = {'help_option_names': ['-h', '--help']}


@click.command(context_settings=context_settings)
@click.option(
    '-f',
    '--format',
    type=click.Choice(['plain', 'json']),
    default='plain',
    show_default=True,
    help='Set format of output.',
)
@click.argument('first_file', type=click.Path(exists=True))
@click.argument('second_file', type=click.Path(exists=True))
def main(first_file, second_file, format):  # noqa: WPS125
    """Generate diff.

    Args:
        first_file (str): Plain json file for comparison.
        second_file (str): Plain json file for comparison.
        format (str): Output format.
    """
    diff = generate_diff.generate_diff(first_file, second_file)
    print(diff)


if __name__ == '__main__':
    main()
