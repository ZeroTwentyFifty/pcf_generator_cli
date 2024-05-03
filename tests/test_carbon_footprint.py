import pytest
from pcf_generator_cli.carbon_footprint import CarbonFootprint

def test_carbon_footprint_exists():
    assert CarbonFootprint is not None

def test_carbon_footprint_instantiation():
    carbon_footprint = CarbonFootprint("kg", 1.0, 0.5, 0.3, 0.2, 0.1, "AR6", ["AR6"], ["Standard"])
    assert isinstance(carbon_footprint, CarbonFootprint)

def test_carbon_footprint_attributes():
    carbon_footprint = CarbonFootprint("kg", 1.0, 0.5, 0.3, 0.2, 0.1, "AR6", ["AR6"], ["Standard"])
    assert carbon_footprint.declared_unit == "kg"
    assert carbon_footprint.unitary_product_amount == 1.0
    assert carbon_footprint.p_cf_excluding_biogenic == 0.5
    assert carbon_footprint.fossil_ghg_emissions == 0.3
    assert carbon_footprint.fossil_carbon_content == 0.2
    assert carbon_footprint.biogenic_carbon_content == 0.1
    assert carbon_footprint.characterization_factors == "AR6"
    assert carbon_footprint.ipcc_characterization_factors_sources == ["AR6"]
    assert carbon_footprint.cross_sectoral_standards_used == ["Standard"]

def test_carbon_footprint_invalid_ipcc_characterization_factors_sources():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, 0.5, 0.3, 0.2, 0.1, "AR6", [], ["Standard"])

def test_carbon_footprint_invalid_unitary_product_amount():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 0.0, 0.5, 0.3, 0.2, 0.1, "AR6", ["AR6"], ["Standard"])

def test_carbon_footprint_invalid_p_cf_excluding_biogenic():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, -0.5, 0.3, 0.2, 0.1, "AR6", ["AR6"], ["Standard"])

def test_carbon_footprint_invalid_fossil_ghg_emissions():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, 0.5, -0.3, 0.2, 0.1, "AR6", ["AR6"], ["Standard"])

def test_carbon_footprint_invalid_fossil_carbon_content():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, 0.5, 0.3, -0.2, 0.1, "AR6", ["AR6"], ["Standard"])

def test_carbon_footprint_invalid_biogenic_carbon_content():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, 0.5, 0.3, 0.2, -0.1, "AR6", ["AR6"], ["Standard"])

def test_carbon_footprint_invalid_characterization_factors():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, 0.5, 0.3, 0.2, 0.1, "", ["AR6"], ["Standard"])

def test_carbon_footprint_invalid_cross_sectoral_standards_used():
    with pytest.raises(ValueError):
        CarbonFootprint("kg", 1.0, 0.5, 0.3, 0.2, 0.1, "AR6", ["AR6"], [])