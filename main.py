import uuid
from datetime import datetime

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--company-name", prompt="Company name", help="The company name.")
@click.option("--status", prompt="Status", help="The status of the product carbon footprint.", type=click.Choice(["Active", "Deprecated"], case_sensitive=False))
@click.option("--spec-version", prompt="Spec version", help="The specification version.", type=click.Choice(["2.0.0", "2.1.0", "2.2.0"]))
@click.option("--company-ids", prompt="Company IDs", help="The company IDs.")
@click.option("--product-description", prompt="Product description", help="The product description.")
@click.option("--product-ids", prompt="Product IDs", help="The product IDs.")
@click.option("--product-category-cpc", prompt="Product category CPC", help="The product category CPC.")
@click.option("--product-name-company", prompt="Product name company", help="The product name company.")
def create(company_name, status, spec_version, company_ids, product_description, product_ids, product_category_cpc, product_name_company):
    """Create a new product carbon footprint."""
    pcf = {
        "id": str(uuid.uuid4()),
        "specVersion": spec_version,
        "version": 1,
        "created": datetime.now().isoformat() + "Z",
        "status": status,
        "companyName": company_name,
        "companyIds": company_ids.split(","),
        "productDescription": product_description,
        "productIds": product_ids.split(","),
        "productCategoryCpc": product_category_cpc,
        "productNameCompany": product_name_company,
        "comment": ""
    }
    click.echo(pcf)


if __name__ == "__main__":
    cli()
