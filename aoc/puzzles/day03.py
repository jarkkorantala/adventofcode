from functools import reduce
from string import ascii_letters as abc
import click
from ..cli import cli, logger, input_iter


@cli.command(help="Day 3: Rucksack Reorganization")
@click.argument("input_path", type=click.Path())
def day03a(input_path):
    priority_sum = 0
    logger.debug(input_path)
    for sack in input_iter(input_path):
        size = int(len(sack) / 2)  # Expect even
        logger.debug(f"{sack!r}, {size!r}")
        a, b = map(set, (sack[:size], sack[size:]))
        logger.debug(f"{a!r}, {b!r}")
        common = a & b
        logger.debug(f"{common!r}, {list(abc.index(c)+1 for c in common)}")
        priority_sum += sum(abc.index(c) + 1 for c in common)
    click.echo(priority_sum)


@cli.command(help="Day 3: Rucksack Reorganization, Part Two")
@click.argument("input_path", type=click.Path())
def day03b(input_path):
    priority_sum = 0
    bags = input_iter(input_path)
    groups = zip(*[iter(bags)] * 3)
    for group in groups:
        group_bags = map(set, group)
        if not group_bags:
            break
        common = reduce(set.intersection, group_bags)
        logger.debug(f"{common!r}, {list(abc.index(c)+1 for c in common)}")
        priority_sum += sum(abc.index(c) + 1 for c in common)
    click.echo(priority_sum)
