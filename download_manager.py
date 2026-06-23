import asyncio

import aiohttp


class Logging:
    def __enter__(self):
        print("Download Started...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Downloaded.\n")


class Manager:
    def __init__(self):
        self.urls = []
        self.successful = 0
        self.failed = 0

    def add(self, url):
        self.urls.append(url)

    @property
    def total_urls(self):
        return len(self.urls)

    @property
    def success_count(self):
        return self.successful

    @property
    def failed_count(self):
        return self.failed

    async def download(self, session, url):
        with Logging():
            try:
                async with session.get(url) as response:
                    print(f"URL: {url}")
                    print(f"Status: {response.status}")

                    await response.text()

                    if response.status == 200:
                        self.successful += 1
                    else:
                        self.failed += 1

            except Exception as e:
                self.failed += 1
                print(f"Error downloading {url}: {e}")

    async def download_all(self):
        async with aiohttp.ClientSession() as session:
            coroutines = []

            for url in self.urls:
                coroutines.append(self.download(session, url))

            await asyncio.gather(*coroutines)


async def main():
    manager = Manager()

    manager.add("https://example.com")
    manager.add("https://google.com")
    manager.add("https://github.com")

    print("Total URLs:", manager.total_urls)
    print()

    await manager.download_all()

    print("Success:", manager.success_count)
    print("Failed:", manager.failed_count)


asyncio.run(main())
