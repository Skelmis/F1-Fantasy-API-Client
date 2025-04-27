import asyncio
import os

from fantasy import APIClient


async def main():
    client: APIClient = await APIClient.login(
        os.environ["username"], os.environ["password"]
    )


if __name__ == "__main__":
    asyncio.run(main())
