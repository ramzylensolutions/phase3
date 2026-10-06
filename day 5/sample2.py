import asyncio
import time
async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 finished")
async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")
async def main():
    await task1()
    await task2()
asyncio.run(main())