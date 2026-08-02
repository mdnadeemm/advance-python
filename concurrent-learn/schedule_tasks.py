import asyncio

async def task1():
    print("Task1 Start")
    await asyncio.sleep(2)
    print("Task2 End")

async def task2():
    print("Task 2 start")
    await asyncio.sleep(2)
    print("Task 2 End")

async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await t1
    await t2

asyncio.run(main())
