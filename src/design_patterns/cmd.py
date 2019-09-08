import click

from design_patterns.version import __version__


@click.group()
def cli():
    click.echo('version %s' % __version__)


@cli.command()
def banana():
    print('banana activated')

    
@cli.command()
def mango():
    print('mango activated')
