import asyncio
async def numbers():
    print("started")
    for i in range(3):
        await asyncio.sleep(5)
        yield i
async def hello():
    print("Started execution")
    await asyncio.sleep(3)
    print("waiting finished")
    await asyncio.sleep(3)
    print("aaa")
async def numbersprint():
    async for i in numbers():
        print(i)
async def main():
    task1 = asyncio.create_task(hello())
    await task1
    task2 = asyncio.create_task(numbersprint())
    await task2
    
    
asyncio.run(main())
