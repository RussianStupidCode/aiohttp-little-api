from aiohttp import hdrs, BasicAuth
from db.models import User


class Auth:
    @staticmethod
    def get_auth(request):
        auth_header = request.headers.get(hdrs.AUTHORIZATION)
        if not auth_header:
            return None
        try:
            auth = BasicAuth.decode(auth_header=auth_header)
        except ValueError:
            auth = None
        return auth

    @staticmethod
    async def get_user(requests):
        auth = Auth.get_auth(requests)
        if not auth:
            return None
        return await User.query.where(User.username == auth.login).gino.first()

    @staticmethod
    async def is_login(requests):
        auth = Auth.get_auth(requests)
        user = await Auth.get_user(requests)

        if not user:
            return False

        return user.check_password(auth.password)