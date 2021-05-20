import click
from aiohttp import web

from sms.routes import setup_routes


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=3000)
def serve(host: str, port: int) -> None:
    app = web.Application()
    setup_routes(app)
    web.run_app(app, host=host, port=port)
