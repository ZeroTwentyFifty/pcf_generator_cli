import pytest
from click.testing import CliRunner
from main import cli

def test_create_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "Active", "--spec-version", "2.0.0"])
    assert result.exit_code == 0
    assert "My Corp" in result.output
    assert "Active" in result.output
    assert "2.0.0" in result.output

def test_create_command_with_invalid_status():
    runner = CliRunner()
    result = runner.invoke(cli, ["create", "--company-name", "My Corp", "--status", "NotAllowed", "--spec-version", "2.0.0"])
    assert result.exit_code != 0
    assert "Invalid value for '--status'" in result.output
