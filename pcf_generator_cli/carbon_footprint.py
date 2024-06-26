import warnings

class CarbonFootprint:
    """
    A CarbonFootprint represents the carbon footprint of a product and related data in accordance with the Pathfinder Framework.

    Attributes:
        declared_unit (str): The unit of analysis of the product.
        unitary_product_amount (float): The amount of Declared Units contained within the product to which the PCF is referring to.
        p_cf_excluding_biogenic (float): The product carbon footprint of the product excluding biogenic CO2 emissions.
        fossil_ghg_emissions (float): The emissions from fossil sources as a result of fuel combustion, from fugitive emissions, and from process emissions.
        fossil_carbon_content (float): The fossil carbon content of the product (mass of carbon).
        biogenic_carbon_content (float): The biogenic carbon content of the product (mass of carbon).
        characterization_factors (str): This property is DEPRECATED and only kept to ensure backwards-compatibility. It will be removed in version 3 of these Technical Specifications.
        ipcc_characterization_factors_sources (list[str]): The characterization factors from one or more IPCC Assessment Reports used in the calculation of the PCF.
        cross_sectoral_standards_used (list[str]): The cross-sectoral standards applied for calculating or allocating GHG emissions.
    """
    def __init__(self, declared_unit, unitary_product_amount, p_cf_excluding_biogenic, fossil_ghg_emissions, fossil_carbon_content, biogenic_carbon_content, characterization_factors, ipcc_characterization_factors_sources, cross_sectoral_standards_used, boundary_processes_description):
        accepted_declared_units = ['liter', 'kilogram', 'cubic meter', 'kilowatt hour', 'megajoule', 'ton kilometer',
                                   'square meter']
        if declared_unit not in accepted_declared_units:
            raise ValueError(
                f"declared_unit '{declared_unit}' is not valid. It must be one of the following: {', '.join(accepted_declared_units)}")
        if unitary_product_amount <= 0:
            raise ValueError("unitary_product_amount must be strictly greater than 0")
        if p_cf_excluding_biogenic < 0:
            raise ValueError("p_cf_excluding_biogenic must be equal to or greater than 0")
        if fossil_ghg_emissions < 0:
            raise ValueError("fossil_ghg_emissions must be equal to or greater than 0")
        if fossil_carbon_content < 0:
            raise ValueError("fossil_carbon_content must be equal to or greater than 0")
        if biogenic_carbon_content < 0:
            raise ValueError("biogenic_carbon_content must be equal to or greater than 0")
        if not characterization_factors:
            raise ValueError("characterization_factors must not be empty")
        if not ipcc_characterization_factors_sources:
            raise ValueError("ipcc_characterization_factors_sources must not be empty")
        if not cross_sectoral_standards_used:
            raise ValueError("cross_sectoral_standards_used must not be empty")
        if not boundary_processes_description:
            raise ValueError("boundary_processes_description must not be empty")

        self.declared_unit = declared_unit
        self.unitary_product_amount = unitary_product_amount
        self.p_cf_excluding_biogenic = p_cf_excluding_biogenic
        self.fossil_ghg_emissions = fossil_ghg_emissions
        self.fossil_carbon_content = fossil_carbon_content
        self.biogenic_carbon_content = biogenic_carbon_content
        self.characterization_factors = characterization_factors
        self.ipcc_characterization_factors_sources = ipcc_characterization_factors_sources
        self.cross_sectoral_standards_used = cross_sectoral_standards_used
        self.boundary_processes_description = boundary_processes_description

        warnings.warn(
            "The 'boundary_processes_description' attribute will become optional in version 3 of the Technical Specifications.",
            PendingDeprecationWarning)
