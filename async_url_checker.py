import asyncio

import aiohttp


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(url, response.status)


async def main():
    urls = ["https://google.com", "https://github.com", "https://openai.com"]

    tasks = []

    for url in urls:
        tasks.append(check(url))
    await asyncio.gather(*tasks)


asyncio.run(main())
