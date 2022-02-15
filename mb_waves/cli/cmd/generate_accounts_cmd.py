import click
import pydash

from mb_waves.cli.helpers import print_json
from mb_waves.waves import account


@click.command(name="generate-accounts", help="Generate new accounts")
@click.option("--limit", "-l", type=int, default=5)
@click.option("--no-seed", is_flag=True, help="Don't output seed")
def cli(limit: int, no_seed: bool):
    result = []
    for _ in range(limit):
        new_acc = account.generate_new_account().dict()
        if no_seed:
            new_acc = pydash.omit(new_acc, "seed")
        result.append(new_acc)
    print_json(result)
