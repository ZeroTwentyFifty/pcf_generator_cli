import json

import pytest
from click.testing import CliRunner

from main import cli


def test_create_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--version", 1, "--company-name", "My Corp", "--status", "Active", "--spec-version", "2.0.0", "--company-ids", "urn:uuid:69585GB6-56T9-6958-E526-6FDGZJHU1326,urn:epc:id:sgln:562958.00000.4", "--product-description", "Bio-Ethanol 98%, corn feedstock (bulk - no packaging)", "--product-ids", "urn:gtin:5695872369587", "--product-category-cpc", "6398", "--product-name-company", "Green Ethanol"])
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
    result = runner.invoke(cli, ["create", "--version", 1, "--company-name", "My Corp", "--status", "NotAllowed", "--spec-version", "2.0.0"])
    assert result.exit_code != 0
    assert "Invalid value for '--status'" in result.output


def test_create_command_with_invalid_spec_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "Active", "--spec-version", "3.0.0"])
    assert result.exit_code != 0
    assert "Invalid value for '--spec-version'" in result.output


def test_create_command_with_invalid_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "Active", "--spec-version", "2.0.0", "--version", "-1"])
    assert result.exit_code != 0
    assert "Version must be in the inclusive range of 0..2^31-1" in result.output


def test_create_command_with_non_integer_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "Active", "--spec-version", "2.0.0", "--version", "abc"])
    assert result.exit_code != 0
    assert "Version must be an integer" in result.output


def test_create_command_with_pretty_print():
    runner = CliRunner()
    result = runner.invoke(cli, [
        "create", "--version", 1, "--company-name", "My Corp", "--status", "Active",
        "--spec-version", "2.0.0", "--company-ids", "MyCorpId", "--product-description", "description",
        "--product-ids", "product-ids", "--product-category-cpc", "12345",
        "--product-name-company", "abc", "--pretty"])
    assert result.exit_code == 0

    # Load the output as JSON and check for the expected structure (Adapt as needed)
    output_json = json.loads(result.output)
    assert output_json['companyName'] == "My Corp"
