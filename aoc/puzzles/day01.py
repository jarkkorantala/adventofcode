import click
import heapq
from ..cli import cli, logger


def build_elf_heap(input_path: str) -> list:
    fp = open(input_path, "r")
    elf_carries = 0
    elf_heap: list[int]  = []
    while True:
        line = fp.readline()
        if "\n" not in line:
            break
        try:
            elf_carries += int(line.strip())
        except Exception:
            logger.debug(f"{elf_carries!r}")
            heapq.heappush(elf_heap, elf_carries)
            elf_carries = 0
    return elf_heap


@cli.command("day01a", help="Day 1: Calorie Counting")
@click.argument("input_path", type=click.Path())
def day01a(input_path):
    elf_heap = build_elf_heap(input_path)
    click.echo(sum(heapq.nlargest(1, elf_heap)))


@cli.command("day01b", help="Day 1: Calorie Counting (sum of top 3)")
@click.argument("input_path", type=click.Path())
def day01b(input_path):
    elf_heap = build_elf_heap(input_path)
    click.echo(sum(heapq.nlargest(3, elf_heap)))
