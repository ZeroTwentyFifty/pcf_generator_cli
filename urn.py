import re


class URN:
    """
    A class representing a generic URN (RFC8141).
    """

    def __init__(self, value: str):
        self.value = value
        self._validate()

    def _validate(self):
        if not re.match(r"^urn:[a-zA-Z0-9][a-zA-Z0-9-]{0,31}:(.*)$", self.value):
            raise ValueError("Value must be a valid URN")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"URN(value='{self.value}')"
