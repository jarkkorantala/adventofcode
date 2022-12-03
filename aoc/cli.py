import click
import logging
import sys
from typing import Generator

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
    )
)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def input_iter(input_path: str) -> Generator[str, None, None]:
    with open(input_path, "r") as fp:
        while True:
            line = fp.readline()
            if "\n" not in line:
                break
            yield line.strip()


@click.group("adventofcode")
@click.option(
    "-d",
    "--debug",
    is_flag=True,
    show_default=True,
    default=False,
    help="Enable debug logging",
)
def cli(debug: bool):
    if debug:
        logger.setLevel(logging.DEBUG)
