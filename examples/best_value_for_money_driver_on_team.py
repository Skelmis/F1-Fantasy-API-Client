import os
import asyncio

from fantasy import Client, APIClient


async def main():
    """Shows who your best driver is by F1's value for money calculation."""
    client = Client(
        APIClient(
            user_guid=os.environ["USER_GUID"],
            token=os.environ["TOKEN"],
        )
    )

    team_to_check = "<TEAM ID HERE>"
    current_race_id = await client.api.get_current_race_id()
    team = await client.fetch_team_info(team_to_check, current_race_id)
    best_value_driver: models.Driver = None  # type: ignore
    for driver in team.drivers:
        if best_value_driver is None:
            best_value_driver = driver
            continue

        if driver.value_for_money is None:
            continue

        if driver.value_for_money > best_value_driver.value_for_money:
            best_value_driver = driver

    print(
        f"The best value for money driver on your team is {best_value_driver.full_name} "
        f"with a value of {best_value_driver.value_for_money}"
    )


if __name__ == "__main__":
    asyncio.run(main())
