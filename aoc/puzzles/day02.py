import click
from ..cli import cli, logger, input_iter


@cli.command(help="Day 2: Rock Paper Scissors")
@click.argument("input_path", type=click.Path())
def day02a(input_path):
    pair_values = {
        "A X": 1 + 3,  # rock ties with rock
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,  # rock loses to paper
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,  # rock beats scissors
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }
    score = 0
    for line in input_iter(input_path):
        score += pair_values[line]
    click.echo(score)


@cli.command(help="Day 2: Rock Paper Scissors, Part Two")
@click.argument("input_path", type=click.Path())
def day02b(input_path):

    pair_values = {
        "A X": 3 + 0,  # lose with scissors
        "A Y": 1 + 3,  # tie with rock
        "A Z": 2 + 6,  # win with paper
        "B X": 1 + 0,  # lose with rock
        "B Y": 2 + 3,  # tie with paper
        "B Z": 3 + 6,  # win with scissors
        "C X": 2 + 0,  # lose with paper
        "C Y": 3 + 3,  # tie with scissors,
        "C Z": 1 + 6,  # win with rock
    }
    score = 0
    for line in input_iter(input_path):
        score += pair_values[line]
        logger.debug(f"{line!r}: {pair_values[line]}")
    click.echo(score)
