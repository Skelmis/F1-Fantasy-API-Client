from __future__ import annotations

from typing import List

from pydantic import BaseModel, ConfigDict, Field

from fantasy.api_models.encoder import URLEncodedStr, BaseAPIModel


class PlayeridItem(BaseAPIModel):
    id: str
    isfinal: int
    iscaptain: int
    ismgcaptain: int
    playerpostion: int


class TeamInfo(BaseAPIModel):
    teamBal: float
    teamVal: float
    maxTeambal: float
    subsallowed: int
    userSubsleft: int


class UserTeamItem(BaseAPIModel):
    gdrank: int | None
    ovrank: int
    teamno: int
    teambal: float
    teamval: float = Field(default=None)
    gdpoints: float | None
    matchday: int
    ovpoints: float
    playerid: List[PlayeridItem]
    teamname: URLEncodedStr
    usersubs: int
    boosterid: int | None
    team_info: TeamInfo
    fttourgdid: int
    fttourmdid: int
    iswildcard: int | None
    maxteambal: float = Field(default=None)
    capplayerid: str
    subsallowed: int
    isaccounting: int
    usersubsleft: int
    extrasubscost: int
    islateonboard: int | None
    mgcapplayerid: None
    race_category: None
    finalfxracecat: None
    finalfxraceday: None
    isboostertaken: int | None
    extradrstakengd: int | None
    finalfixtakengd: int | None
    isextradrstaken: int | None
    isfinalfixtaken: int | None
    iswildcardtaken: int | None
    wildcardtakengd: int | None
    autopilottakengd: int | None
    isautopilottaken: int | None
    islimitlesstaken: int | None
    limitlesstakengd: int | None
    isnonigativetaken: int | None
    nonigativetakengd: int | None
    finalfxnewplayerid: None
    finalfxoldplayerid: None
    player_swap_details: None
    is_wildcard_taken_gd_id: int | None
    inactive_driver_penality_points: int


class LeagueTeam(BaseAPIModel):
    mdid: int
    userTeam: List[UserTeamItem]
    retval: int
