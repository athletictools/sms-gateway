from aiohttp.web import Application

from sms import handlers


async def app_factory() -> Application:
    app = Application()
    setup_routes(app)
    return app


def setup_routes(app: Application):
    app.router.add_post('/send', handlers.send_sms)
