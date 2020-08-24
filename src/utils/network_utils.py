import aiohttp

default_headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept-Language': 'ru-RU'
}


async def post(url, json_payload=None, data=None, headers=None):
    if headers is None:
        headers = default_headers
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=json_payload, data=data) as resp:
            return await resp.json() or resp.text()
