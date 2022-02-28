from app.views.user import *
from app.views.advertisement import *
from aiohttp import web
from db.models import User
from db.data_base import data_base as db
from app.application import aiohttp_app


async def health(request: web.Request):
    if request.method == 'GET':
        return web.json_response({'status': 'OK'})

    return web.json_response({'status': 'OK'})


aiohttp_app.add_routes([web.get("/health", health)])