import uuid
from datetime import datetime


class ProductCarbonFootprint:
    def __init__(self, company_name, status, spec_version, version, company_ids, product_description, product_ids, product_category_cpc, product_name_company):
        self.id = str(uuid.uuid4())
        self.spec_version = spec_version
        self.version = version
        self.created = datetime.now().isoformat() + "Z"
        self.status = status
        self.company_name = company_name
        self.company_ids = company_ids
        self.product_description = product_description
        self.product_ids = product_ids
        self.product_category_cpc = product_category_cpc
        self.product_name_company = product_name_company
        self.comment = ""

    def to_dict(self):
        """Converts the ProductCarbonFootprint object to a dictionary."""
        return {
            "id": self.id,
            "specVersion": self.spec_version,
            "version": self.version,
            "created": self.created,
            "status": self.status,
            "companyName": self.company_name,
            "companyIds": self.company_ids,
            "productDescription": self.product_description,
            "productIds": self.product_ids,
            "productCategoryCpc": self.product_category_cpc,
            "productNameCompany": self.product_name_company,
            "comment": self.comment
        }
