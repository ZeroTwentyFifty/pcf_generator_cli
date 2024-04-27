import uuid
from datetime import datetime


class ProductCarbonFootprint:
    def __init__(self,
                 company_name: str,
                 status: str,
                 spec_version: str,
                 version: int,
                 company_ids: list[str],
                 product_description: str,
                 product_ids: list[str],
                 product_category_cpc: str,
                 product_name_company: str) -> None:

        self.id: str = str(uuid.uuid4())
        self.spec_version: str = spec_version
        self.version: int = version
        self.created: str = datetime.now().isoformat() + "Z"
        self.status: str = status
        self.company_name: str = company_name
        self.company_ids: list[str] = company_ids
        self.product_description: str = product_description
        self.product_ids: list[str] = product_ids
        self.product_category_cpc: str = product_category_cpc
        self.product_name_company: str = product_name_company
        self.comment: str = ""

    def to_dict(self) -> dict:
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
