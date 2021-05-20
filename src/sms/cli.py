import click
from aiohttp import web

from sms.application import app_factory


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=3000)
def serve(host: str, port: int) -> None:
    web.run_app(app_factory, host=host, port=port)
