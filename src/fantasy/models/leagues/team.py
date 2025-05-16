from pydantic import BaseModel

from fantasy.api_models import leagues
from fantasy.models import Driver, Constructor


class TeamEntry(BaseModel):
    """This is either a driver or team"""

    id: str
    has_2x: bool
    has_3x: bool


class TeamInfo(BaseModel):
    team_bal: float
    team_val: float
    max_team_bal: float
    subs_allowed: int
    user_subs_left: int


class LeagueTeam(BaseModel):
    raw_team_entries: list[TeamEntry]
    drivers: list[Driver]
    constructors: list[Constructor]
    global_league_rank: int
    points_from_this_race: float
    overall_points: float
    team_name: str
    current_booster: int | None
    is_using_wild_card: bool
    subs_allowed: int
    user_subs_left: int
    extra_subs_cost: int
    raw_api_model: leagues.LeagueTeam
