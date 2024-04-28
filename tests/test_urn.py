import pytest

from urn import URN

def test_valid_urn():
    urn_string = "urn:isbn:978-0-596-52932-1"
    urn = URN(value=urn_string)
    assert urn.value == urn_string

def test_invalid_urn_format():
    with pytest.raises(ValueError):
        URN(value="not-a-valid-urn")

def test_isbn_urn():
    urn = URN(value="urn:isbn:978-0-596-52932-1")
    assert urn.value == "urn:isbn:978-0-596-52932-1"

def test_uuid_urn():
    urn = URN(value="urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
    assert urn.value == "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6"

@pytest.mark.parametrize(
    "urn_string",
    [
        "urn:pathfinder:company:customcode:buyer-assigned:4321",
        "urn:pathfinder:company:customcode:vendor-assigned:6789",
        "urn:pathfinder:product:customcode:buyer-assigned:1234",
        "urn:pathfinder:product:customcode:vendor-assigned:8765",
        "urn:pathfinder:product:id:cas:64-17-5",
        "urn:pathfinder:product:id:iupac-inchi:1S%2FC9H8O4%2Fc1-6%2810%2913-8-5-3-2-4-7%288%299%2811%2912%2Fh2-5H%2C1H3%2C%28H%2C11%2C12%29"
    ]
)
def test_valid_pathfinder_urns(urn_string):
    urn = URN(value=urn_string)
    assert urn.value == urn_string
