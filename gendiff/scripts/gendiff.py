#!/usr/bin/env python3
"""Gendiff."""
import click

context_settings = {'help_option_names': ['-h', '--help']}


@click.command(context_settings=context_settings)
@click.argument('first_file')
@click.argument('second_file')
def main():
    """Generate diff."""


if __name__ == '__main__':
    main()
