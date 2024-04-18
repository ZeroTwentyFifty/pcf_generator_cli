import click
import uuid
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option("--company-name", prompt="Company name", help="The company name.")
@click.option("--status", prompt="Status", help="The status of the product carbon footprint.", type=click.Choice(["Active", "Deprecated"]))
@click.option("--spec-version", prompt="Spec version", help="The specification version.")
def create(company_name, status, spec_version):
    """Create a new product carbon footprint."""
    pcf = {
        "id": str(uuid.uuid4()),
        "specVersion": spec_version,
        "version": 1,
        "created": datetime.now().isoformat() + "Z",
        "status": status,
        "validityPeriodStart": datetime.now().isoformat() + "Z",
        "validityPeriodEnd": "2024-12-31T00:00:00Z",
        "companyName": company_name
    }
    click.echo(pcf)


if __name__ == "__main__":
    cli()
