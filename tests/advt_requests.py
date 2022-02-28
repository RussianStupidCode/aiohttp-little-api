import aiohttp
import asyncio
from tests.user_requests import create_user


async def create_advt(username: str, password: str):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:80/advt', json={
                         'title': 'hello',
                         'text': "world"
        }, auth=aiohttp.BasicAuth(username, password)) as resp:
            resp_json = await resp.json()
            print("create", resp_json)


async def update_advt(advt_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.patch(f'http://127.0.0.1:80/advt/{advt_id}', json={
                         'title': 'hellooooooo',
        }) as resp:
            resp_json = await resp.json()
            print("update", resp_json)


async def delete_advt(advt_id: int, username: str, password: str):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f'http://127.0.0.1:80/advt/{advt_id}',
                                  auth=aiohttp.BasicAuth(username, password)) as resp:
            resp_json = await resp.json()
            print("delete", resp_json)


async def get_advt(advt_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:80/advt/{advt_id}') as resp:
            resp_json = await resp.json()
            print("get", resp_json)


async def main():
    await create_user("test12345", "123dfsfsdgfD", "ttest@gmail.com")
    await create_advt("test12345", "123dfsfsdgfD")
    await delete_advt(1, "test12345", "123dfsfsdgfD")

if __name__ == "__main__":
    asyncio.run(main())