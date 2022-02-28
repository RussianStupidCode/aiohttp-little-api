import aiohttp
import asyncio


async def healthy():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:80/health') as resp:
            resp_json = await resp.json()
            print("healthy", resp_json)


async def create_user(username: str, password: str, email: str):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:80/user', json={
                         'username': username,
                         'password': password,
                         'email': email
        }) as resp:
            resp_json = await resp.json()
            print("create", resp_json)


async def update_user(user_id: int, username: str):
    async with aiohttp.ClientSession() as session:
        async with session.patch(f'http://127.0.0.1:80/user/{user_id}', json={
                         'username': username,
        }) as resp:
            resp_json = await resp.json()
            print("delete", resp_json)


async def get_user(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:80/user/{user_id}') as resp:
            resp_json = await resp.json()
            print("get", resp_json)


async def delete_user(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f'http://127.0.0.1:80/user/{user_id}') as resp:
            resp_json = await resp.json()
            print("delete", resp_json)


async def main(user_id=1):
    await create_user("test123", "123Addsfasd", "test123@mail.ru")
    await get_user(user_id)
    await update_user(user_id, "test124")
    await get_user(user_id)
    await delete_user(user_id)


if __name__ == "__main__":
    asyncio.run(main(1))
