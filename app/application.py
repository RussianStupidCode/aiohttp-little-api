from aiohttp import web
from sqlalchemy.engine.url import URL
from db import config
from db.data_base import data_base
from db.models import User

aiohttp_app = web.Application()


async def init_orm(app):
    await data_base.set_bind(URL(**config.DATABASE))
    await data_base.gino.create_all()
    yield
    await data_base.pop_bind().close()


aiohttp_app.cleanup_ctx.append(init_orm)
#auth = HTTPBasicAuth()

