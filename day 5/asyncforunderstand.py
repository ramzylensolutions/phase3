import asyncio

async def numbers():
    for i in range(3):
        await asyncio.sleep(4)
        yield i
async def numbers2():
    for i in range(6):
        await asyncio.sleep(2)
        yield "Task 2"
async def task2():
    async for i in numbers2():
        print(i)
async def task1():
    async for i in numbers():
        print(i)
async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    await task_1
    await task_2
asyncio.run(main())