import re

from urnparse import URN8141, InvalidURNFormatError


class URN:
    """
    A class representing a generic URN (RFC8141).
    """

    def __init__(self, value: str):
        self.value = value
        self._validate()

    def _validate(self):
        try:
            URN8141.from_string(self.value)
        except InvalidURNFormatError:
            raise ValueError("Value must be a valid URN")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"URN(value='{self.value}')"


class CompanyId(URN):
    BUYER_ASSIGNED_PATTERN = re.compile(r"^urn:pathfinder:company:customcode:buyer-assigned:[a-zA-Z0-9-]+$")
    VENDOR_ASSIGNED_PATTERN = re.compile(r"^urn:pathfinder:company:customcode:vendor-assigned:[a-zA-Z0-9-]+$")

    def _validate(self):
        super()._validate()  # Inherit URN validation

        if not (self.BUYER_ASSIGNED_PATTERN.match(self.value) or
                self.VENDOR_ASSIGNED_PATTERN.match(self.value)):
            raise ValueError("CompanyId does not conform to the required format")


class ProductId(URN):
    pass  # For now, no additional validation on top of URN
