F1 Fantasy API Client
---

A mildy jank implementation letting you browse the F1 fantasy data set. 

Certain values are basically guaranteed to be wrong and methods are missing due to a lack of public data. Therefore, this is a best guess implementation, and I'd love any feedback.


### Basic Usage

Install it with:
```shell
pip install skelmis-f1-fantasy
```

#### Show current best rankings in private leagues

- Navigate to https://fantasy.formula1.com
- Open dev tools for your browser (typically F12)
- Click `Network`
- Login
- Look for a request to `/services/session/login`
- Click `Response`
- Copy the value of `GUID` and `Token`.
- See below example.

```python
import asyncio

# pip install skelmis-f1-fantasy
from fantasy import Client, APIClient


async def main():
    """Shows your highest place in all your private leagues."""
    client = Client(
        APIClient(
            user_guid="GUID Here",
            token="Token Here",
        )
    )

    user_leagues = await client.get_user_leagues()
    for league in user_leagues.leagues:
        leaderboard = await client.get_private_league_leaderboard(league.league_id)
        ranks = [i.rank_in_league for i in league.teams_in_league]
        print(f"League: {leaderboard.league_name}\n\tBest rank: {max(ranks)}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Further Usage

The class `fantasy.Client` exposes all the nice data models, however many are missing.

If you want full access, use `fantasy.APIClient` which implements significantly more but provides the data as the API does which is hard to work with.