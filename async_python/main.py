import asyncio

# async def do_something() -> str:
#     print("Doing something asynchronously...")
#     return "Done!"

# async def main():
#     print("Starting main function...")
#     await asyncio.sleep(1)  # Simulating some async work
#     result = await do_something()
#     print(result)


## Parallel

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done after {delay}s")
    return name

async def main():
    results = await asyncio.gather(
        task("fetch_data", 1),
        task("process_data", 2),
        task("save_data", 3)
    )
    print(results)

if __name__ == "__main__":
    print("Main function is about to run...")
    asyncio.run(main())
    print("Main function completed.")
