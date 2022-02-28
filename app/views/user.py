from aiohttp import web
from db.models import User
from app.application import aiohttp_app
from app.views.mixin import BaseMixin
from validate.schemas.user import USER_CREATE, USER_UPDATE


class UserView(web.View, BaseMixin):
    @staticmethod
    def _get_user_data(user):
        user_data = user.to_dict()
        user_data.pop("password")
        return user_data

    async def get(self):
        user_id = self._get_item_id()
        user = await User.get(user_id)
        if not user:
            return self._get_not_found()

        return web.json_response(self._get_user_data(user))

    async def post(self):
        user_data = await self.request.json()
        try:
            self.validate(user_data, USER_CREATE)
            user_data['password'] = User.set_password(user_data['password'])
            user = await User.create(**user_data)
            return web.json_response(self._get_user_data(user))
        except Exception as er:
            return self._get_bad_luck()

    async def delete(self):
        user_id = self._get_item_id()
        user = await User.get(user_id)

        if not user:
            return self._get_not_found()

        await user.delete()
        return web.json_response({'status': 'OK'})

    async def patch(self):
        user_id = self._get_item_id()
        user_data = await self.request.json()
        try:
            self.validate(user_data, USER_UPDATE)
        except Exception as er:
            return self._get_bad_luck()

        user = await User.get(user_id)

        if not user:
            return self._get_not_found()

        await user.update(**user_data).apply()
        return web.json_response(self._get_user_data(user))


aiohttp_app.add_routes([
    web.get("/user/{item_id:\d+}", UserView),
    web.post("/user", UserView),
    web.patch("/user/{item_id:\d+}", UserView),
    web.delete("/user/{item_id:\d+}", UserView)
])