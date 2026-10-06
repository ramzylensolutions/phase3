import asyncio

class MyResource:
    async def __aenter__(self):
        print("Resource opened")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Resource closed")

async def main():
    async with MyResource():
        print("Using resource")

asyncio.run(main())