import pytest
from click.testing import CliRunner

from main import cli


def test_create_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "Active", "--spec-version", "2.0.0", "--company-ids", "urn:uuid:69585GB6-56T9-6958-E526-6FDGZJHU1326,urn:epc:id:sgln:562958.00000.4", "--product-description", "Bio-Ethanol 98%, corn feedstock (bulk - no packaging)", "--product-ids", "urn:gtin:5695872369587", "--product-category-cpc", "6398", "--product-name-company", "Green Ethanol"])
    assert result.exit_code == 0
    assert "My Corp" in result.output
    assert "Active" in result.output
    assert "2.0.0" in result.output
    assert "urn:uuid:69585GB6-56T9-6958-E526-6FDGZJHU1326" in result.output
    assert "urn:epc:id:sgln:562958.00000.4" in result.output
    assert "Bio-Ethanol 98%, corn feedstock (bulk - no packaging)" in result.output
    assert "urn:gtin:5695872369587" in result.output
    assert "6398" in result.output
    assert "Green Ethanol" in result.output


def test_create_command_with_invalid_status():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "NotAllowed", "--spec-version", "2.0.0"])
    assert result.exit_code != 0
    assert "Invalid value for '--status'" in result.output
