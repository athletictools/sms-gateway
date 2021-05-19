import click
from aiohttp import web


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--host', type=str, default='127.0.0.1')
@click.option('--port', type=int, default=3000)
def serve(host: str, port: int) -> None:
    app = web.Application()
    web.run_app(app, host=host, port=port)
