import asyncio

import aiohttp


async def scrape(session, url):

    try:
        async with session.get(url) as response:
            print(response)
    except Exception as e:
        print(url, e)


async def main():

    # dummy urls
    urls = ["https://www.example.com" for _ in range(100)]
    async with aiohttp.ClientSession() as session:
        tasks = [scrape(session, url) for url in urls]

        await asyncio.gather(*tasks)


asyncio.run(main())
