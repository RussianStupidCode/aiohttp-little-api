import os
from app.application import aiohttp_app
from app.views import app
from aiohttp import web

if __name__ == "__main__":
    web.run_app(aiohttp_app, host="0.0.0.0", port=80)