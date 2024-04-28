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
