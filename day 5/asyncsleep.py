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
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    await task_1
    await task_2
asyncio.run(main())