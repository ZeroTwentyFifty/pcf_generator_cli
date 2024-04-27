import pytest

from pcf import ProductCarbonFootprint


def test_pcf_creation():
    pcf = ProductCarbonFootprint(
        "My Corp", "Active", "2.0.0", 1, ["company_id"], "Description",
        ["product_id"], "12345", "Product Name"
    )
    assert isinstance(pcf.id, str)
    assert pcf.spec_version == "2.0.0"
    assert pcf.status == "Active"

def test_to_dict():
    pcf = ProductCarbonFootprint(
        "My Corp", "Active", "2.0.0", 1, ["company_id"], "Description",
        ["product_id"], "12345", "Product Name"
    )
    output_dict = pcf.to_dict()
    assert "id" in output_dict
    assert "companyName" in output_dict
