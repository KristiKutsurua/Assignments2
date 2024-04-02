import asyncio
import time

async def delay_2_seconds():
    print("Task 1 started at:", time.strftime("%H:%M:%S"))
    await asyncio.sleep(2)
    print("Task 1 ended at:", time.strftime("%H:%M:%S"))

async def delay_5_seconds():
    print("Task 2 started at:", time.strftime("%H:%M:%S"))
    await asyncio.sleep(5)
    print("Task 2 ended at:", time.strftime("%H:%M:%S"))

async def main():
    task1 = asyncio.create_task(delay_2_seconds())
    task2 = asyncio.create_task(delay_5_seconds())
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
