import pytest

from pcf import ProductCarbonFootprint


def test_pcf_creation():
    pcf = ProductCarbonFootprint(
        "My Corp", "Active", "2.0.0", 1, ["company_id"], "Description",
        ["product_id"], "12345", "Product Name"
    )

    assert isinstance(pcf.id, str) and len(pcf.id) > 0
    assert pcf.spec_version == "2.0.0"
    assert pcf.status == "Active"
    assert pcf.version == 1
    assert isinstance(pcf.created, str)
    assert pcf.company_name == "My Corp"
    assert pcf.company_ids == ["company_id"]
    assert pcf.product_description == "Description"
    assert pcf.product_ids == ["product_id"]
    assert pcf.product_category_cpc == "12345"
    assert pcf.product_name_company == "Product Name"
    assert pcf.comment == ""


def test_to_dict():
    pcf = ProductCarbonFootprint(
        "My Corp", "Active", "2.0.0", 1, ["company_id"], "Description",
        ["product_id"], "12345", "Product Name"
    )

    output_dict = pcf.to_dict()

    assert "id" in output_dict
    assert "companyName" in output_dict
    assert "specVersion" in output_dict
    assert "version" in output_dict
    assert "created" in output_dict
    assert "status" in output_dict
    assert "companyIds" in output_dict
    assert "productDescription" in output_dict
    assert "productIds" in output_dict
    assert "productCategoryCpc" in output_dict
    assert "productNameCompany" in output_dict
    assert "comment" in output_dict
