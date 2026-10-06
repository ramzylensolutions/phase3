import asyncio
async def numbers():
    for i in range(3):
        await asyncio.sleep(2)
        yield i
async def main():
    async for number in numbers():
        print(number)
asyncio.run(main())