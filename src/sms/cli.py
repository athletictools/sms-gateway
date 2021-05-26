import click

from sms.handlers import app

@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=3000)
def serve(host: str, port: int) -> None:
    app
