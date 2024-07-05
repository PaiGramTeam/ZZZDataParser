from src.main import main as main_src


async def main():
    await main_src()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
