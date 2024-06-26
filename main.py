import json

import click

from pcf import ProductCarbonFootprint


def validate_version(ctx, param, value):
    try:
        version = int(value)
        if not 0 <= version <= 2**31-1:
            raise click.BadParameter("Version must be in the inclusive range of 0..2^31-1")
    except ValueError:
        raise click.BadParameter("Version must be an integer")
    return value


def validate_product_category_cpc(ctx, param, value):
    if not value.isdigit():
        raise click.BadParameter("Product category CPC must be a numerical value.")
    if len(value) > 5:
        raise click.BadParameter("Product category CPC cannot exceed 5 characters.")
    return value


@click.group()
def cli():
    pass


@cli.command()
@click.option("--company-name", prompt="Company name", help="The company name.")
@click.option("--status", prompt="Status", help="The status of the product carbon footprint.", type=click.Choice(["Active", "Deprecated"], case_sensitive=False))
@click.option("--version", prompt="Version", help="The version.", callback=validate_version)
@click.option("--spec-version", prompt="Spec version", help="The specification version.", type=click.Choice(["2.0.0", "2.1.0", "2.2.0"]))
@click.option("--company-ids", prompt="Company IDs", help="The company IDs.")
@click.option("--product-description", prompt="Product description", help="The product description.")
@click.option("--product-ids", prompt="Product IDs", help="The product IDs.")
@click.option("--product-category-cpc", prompt="Product category CPC", help="The product category CPC.", callback=validate_product_category_cpc)
@click.option("--product-name-company", prompt="Product name company", help="The product name company.")
@click.option("--pretty", is_flag=True, default=False, help="Pretty-print the output.")
def create(
        company_name, status, spec_version, version, company_ids, product_description,
        product_ids, product_category_cpc, product_name_company, pretty):
    """Create a new product carbon footprint."""

    pcf = ProductCarbonFootprint(
        company_name, status, spec_version, version,
        company_ids.split(","), product_description,
        product_ids.split(","), product_category_cpc,
        product_name_company
    )

    if pretty:
        click.echo(json.dumps(pcf.to_dict(), indent=4))
    else:
        click.echo(pcf.to_dict())


if __name__ == "__main__":
    cli()
