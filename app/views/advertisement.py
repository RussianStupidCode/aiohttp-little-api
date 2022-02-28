from db.models import Advertisement, User
from aiohttp import web
from app.views.mixin import BaseMixin
from validate.schemas.advertisement import ADVT_CREATE, ADVT_UPDATE
from app.views.auth import Auth
from app.application import aiohttp_app


class AdvertisementView(web.View, BaseMixin):
    @staticmethod
    def get_auth_error():
        response = web.json_response({'message': 'unauthorized'})
        response.set_status(401)
        return response

    async def get(self):
        advt_id = self._get_item_id()
        advt = await Advertisement.get(advt_id)
        if not advt:
            return self._get_not_found()

        return web.json_response(advt.to_dict())

    async def post(self):
        if not await Auth.is_login(self.request):
            return self.get_auth_error()

        data = await self.request.json()
        user = await Auth.get_user(self.request)

        try:
            self.validate(data, ADVT_CREATE)
            data["owner_id"] = user.id
            advt = await Advertisement.create(**data)
            return web.json_response(advt.to_dict())
        except Exception as er:
            return self._get_bad_luck()

    async def delete(self):
        if not await Auth.is_login(self.request):
            return self.get_auth_error()

        user = await Auth.get_user(self.request)
        advt_id = self._get_item_id()
        advt = await Advertisement.get(advt_id)

        if not user:
            return self._get_not_found()

        if user.id != advt.owner_id:
            return self._get_bad_luck()

        await advt.delete()
        return web.json_response({'status': 'OK'})


aiohttp_app.add_routes([
    web.get("/advt/{item_id:\d+}", AdvertisementView),
    web.post("/advt", AdvertisementView),
    web.delete("/advt/{item_id:\d+}", AdvertisementView)
])