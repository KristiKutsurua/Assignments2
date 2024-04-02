import asyncio
import random

async def print_numbers():
    delay = random.uniform(1, 5)
    print(f"Delaying for {delay:.2f} seconds")
    await asyncio.sleep(delay)
    print("Printing numbers:")
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(delay)

async def main():
    await print_numbers()

if __name__ == "__main__":
    asyncio.run(main())
