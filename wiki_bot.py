import click

from mylib.bot import scrape

@click.command()
@click.option('--name', default="Wikipedia", help='Page to scrape')
def cli(name="Microsoft", length=1):
    result = scrape(name, length)
    click.echo(click.style(f"{result}", bg="white", fg="black"))
    return result


if __name__ == '__main__':
    cli()
