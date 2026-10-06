import asyncio
def hello():
    return "hello"
print(hello())

async def helloo():
    return "hello"
async def main():
    print(await helloo())
asyncio.run(main())
