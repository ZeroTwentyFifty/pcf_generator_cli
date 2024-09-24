import json

import pytest
from click.testing import CliRunner

from main import cli


def test_create_command_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--help"])
    assert result.exit_code == 0
    assert "Create a new product carbon footprint." in result.output


def test_create_command_invalid_status():
    runner = CliRunner()
    result = runner.invoke(cli,
                           [
                               "create",
                               "--status", "NotAllowed"
                           ]
                           )
    assert result.exit_code != 0
    assert "Invalid value for '--status'" in result.output


def test_create_command_invalid_version():
    runner = CliRunner()
    result = runner.invoke(cli,
                           [
                               "create",
                               "--version", -1
                           ]
                           )
    assert result.exit_code != 0
    assert "Invalid value for '--version'" in result.output


def test_create_command_invalid_spec_version():
    runner = CliRunner()
    result = runner.invoke(cli,
                           [
                               "create",
                               "--spec-version", "3.0.0"
                           ]
                           )
    assert result.exit_code != 0
    assert "Invalid value for '--spec-version'" in result.output


def test_create_command_with_complete_set_of_valid_options():
    runner = CliRunner()
    result = runner.invoke(cli,
                           [
                               "create",
                               "--version", 1,
                               "--company-name", "My Corp",
                               "--status", "Active",
                               "--spec-version", "2.0.0",
                               "--company-ids", "urn:pathfinder:company:customcode:buyer-assigned:acme-corp",
                               "--product-description", "description",
                               "--product-ids", "urn:pathfinder:product:customcode:buyer-assigned:acme-product",
                               "--product-category-cpc", "01142",
                               "--product-name-company", "abc",
                               "--comment", "abc",
                           ]
                           )
    assert result.exit_code == 0


def test_create_command_pretty_print():
    runner = CliRunner()
    result = runner.invoke(cli,
                           [
                               "create",
                               "--version", 1,
                               "--company-name", "My Corp",
                               "--status", "Active",
                               "--spec-version", "2.0.0",
                               "--company-ids", "urn:pathfinder:company:customcode:buyer-assigned:acme-corp",
                               "--product-description", "description",
                               "--product-ids", "urn:pathfinder:product:customcode:buyer-assigned:acme-product",
                               "--product-category-cpc", "01142",
                               "--product-name-company", "abc",
                               "--comment", "abc",
                               "--pretty"
                           ]
                           )
    assert result.exit_code == 0
    try:
        json.loads(result.output)
    except json.JSONDecodeError:
        pytest.fail("Output is not valid JSON")
        