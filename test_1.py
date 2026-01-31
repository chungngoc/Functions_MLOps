from calcul import sum
from mylib.bot import scrape
from wiki_bot import cli
from click.testing import CliRunner

def test_sum():
    assert sum(2,3) == 5

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ['--name', 'Microsoft'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output