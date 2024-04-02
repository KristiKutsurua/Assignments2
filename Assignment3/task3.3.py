import asyncio

async def square_number(number):
    print(f"Calculating square of {number}...")
    await asyncio.sleep(1)
    return number ** 2

async def is_even(number):
    print(f"Checking if {number} is even...")
    await asyncio.sleep(1)
    return number % 2 == 0

async def main():
    numbers = [2, 3, 4, 5, 6]
    tasks = []

    for number in numbers:
        tasks.append(square_number(number))

    for number in numbers:
        tasks.append(is_even(number))

    results = await asyncio.gather(*tasks)

    square_results = results[:len(numbers)]
    even_results = results[len(numbers):]

    print("Square results:")
    for number, result in zip(numbers, square_results):
        print(f"{number} squared is {result}")

    print("\nEven check results:")
    for number, result in zip(numbers, even_results):
        print(f"{number} is even: {result}")

if __name__ == "__main__":
    asyncio.run(main())
