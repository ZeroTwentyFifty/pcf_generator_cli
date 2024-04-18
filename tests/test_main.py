from click.testing import CliRunner
from main import cli


def test_init_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["init"])
    assert result.exit_code == 0
    assert "Initializing a new product carbon footprint..." in result.output