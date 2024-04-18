import click


@click.group()
def cli():
    pass


@cli.command()
def init():
    """Initialize a new product carbon footprint."""
    click.echo("Initializing a new product carbon footprint...")


if __name__ == "__main__":
    cli()
