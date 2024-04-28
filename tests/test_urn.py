import pytest

from urn import URN

def test_valid_urn():
    urn_string = "urn:isbn:978-0-596-52932-1"
    urn = URN(value=urn_string)
    assert urn.value == urn_string

def test_invalid_urn_format():
    with pytest.raises(ValueError):
        URN(value="not-a-valid-urn")

# Add more tests for specific URN schemes as needed