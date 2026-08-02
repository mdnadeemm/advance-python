import asyncio

async def hello():
    print("A")

    await asyncio.sleep(2)
    print("B")
print("1")
asyncio.run(hello())
print("2")
