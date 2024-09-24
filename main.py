import json
from datetime import datetime

import click

from pact_methodology.carbon_footprint.carbon_footprint import CarbonFootprint
from pact_methodology.datetime import DateTime
from pact_methodology.product_footprint.cpc import CPC, CPCCodeLookup
from pact_methodology.product_footprint.product_footprint import ProductFootprint
from pact_methodology.product_footprint.status import ProductFootprintStatus
from pact_methodology.product_footprint.version import Version
from pact_methodology.urn import CompanyId, ProductId


def validate_version(ctx: click.Context, param: click.Option, value: int) -> int:
    """Validates the provided version."""
    if not 0 <= value <= 2**31-1:
        raise click.BadParameter("Version must be in the inclusive range of 0..2^31-1")
    return value


def validate_product_category_cpc(ctx: click.Context, param: click.Option, value: str) -> str:
    """Validates the provided product category CPC."""
    cpc_lookup = CPCCodeLookup()
    cpc = cpc_lookup.lookup(value)
    if cpc is None:
        raise click.BadParameter("Invalid product category CPC")
    return value


@click.group()
def cli() -> None:
    """CLI entry point."""
    pass


@cli.command()
@click.option("--company-name", prompt="Company name", help="The company name.")
@click.option("--status", prompt="Status", help="The status of the product carbon footprint.", type=click.Choice(["Active", "Deprecated"], case_sensitive=False))
@click.option("--version", prompt="Version", help="The version.", callback=validate_version, type=int)
@click.option("--spec-version", prompt="Spec version", help="The specification version.", type=click.Choice(["2.0.0", "2.1.0", "2.2.0"]))
@click.option("--company-ids", prompt="Company IDs", help="The company IDs.")
@click.option("--product-description", prompt="Product description", help="The product description.")
@click.option("--product-ids", prompt="Product IDs", help="The product IDs.")
@click.option("--product-category-cpc", prompt="Product category CPC", help="The product category CPC.", callback=validate_product_category_cpc)
@click.option("--product-name-company", prompt="Product name company", help="The product name company.")
@click.option("--comment", prompt="Comment", help="Comment")
@click.option("--pretty", is_flag=True, default=False, help="Pretty-print the output.")
def create(
    company_name: str,
    status: str,
    spec_version: str,
    version: int,
    company_ids: str,
    product_description: str,
    product_ids: str,
    product_category_cpc: str,
    product_name_company: str,
    comment: str,
    pretty: bool
) -> None:
    """Create a new product carbon footprint."""

    # fill in when availble
    # carbon_footprint = CarbonFootprint(
    #     pass=pass
    # )

    # Create a ProductFootprint object using the provided data
    cpc_lookup = CPCCodeLookup()
    cpc = cpc_lookup.lookup(product_category_cpc)
    product_footprint = ProductFootprint(
        id=None,
        spec_version=spec_version,
        version=Version(version),
        created=DateTime.now(),
        updated=None,
        status=ProductFootprintStatus(status),
        status_comment=None,
        validity_period=None,
        company_name=company_name,
        company_ids=[CompanyId(company_id) for company_id in company_ids.split(",")],
        product_description=product_description,
        product_ids=[ProductId(product_id) for product_id in product_ids.split(",")],
        product_category_cpc=cpc,
        product_name_company=product_name_company,
        comment=comment,
        extensions=None,
        pcf=None,
        preceding_pf_ids=None,
    )

    # Convert the ProductFootprint object to a dictionary
    output_data = product_footprint.__dict__

    # Print the output data in the desired format
    if pretty:
        click.echo(json.dumps(output_data, indent=4, default=str))
    else:
        click.echo(output_data)


if __name__ == "__main__":
    cli()