from typing import Optional

from pydantic import BaseModel

from fantasy.api_models.encoder import URLEncodedStr


class PlayeridItem(BaseModel):
    id: str
    isfinal: int | None
    iscaptain: int | None
    ismgcaptain: int | None
    playerpostion: int | None


class TeamInfo(BaseModel):
    teamBal: float
    teamVal: float
    maxTeambal: float
    subsallowed: int | None
    userSubsleft: int | None


class UserTeamItem(BaseModel):
    gdrank: int | None
    ovrank: int | None
    teamno: int | None
    teambal: float
    teamval: Optional[float] = None
    gdpoints: int | None
    matchday: int | None
    ovpoints: float
    playerid: list[PlayeridItem]
    teamname: URLEncodedStr
    usersubs: int | None
    boosterid: int | None
    team_info: TeamInfo
    fttourgdid: int | None
    fttourmdid: int | None
    iswildcard: Optional[int]
    maxteambal: Optional[float] = None
    capplayerid: str
    subsallowed: int | None
    isaccounting: int | None
    usersubsleft: int | None
    extrasubscost: int | None
    islateonboard: Optional[int]
    mgcapplayerid: int | None
    race_category: int | None
    finalfxracecat: int | None
    finalfxraceday: int | None
    isboostertaken: Optional[int]
    extradrstakengd: int | None
    finalfixtakengd: int | None
    isextradrstaken: int | None
    isfinalfixtaken: int | None
    issystemnameupd: int | None
    iswildcardtaken: int | None
    wildcardtakengd: int | None
    autopilottakengd: int | None
    isautopilottaken: int | None
    islimitlesstaken: int | None
    limitlesstakengd: int | None
    isnonigativetaken: int | None
    iswebpurifycalled: int | None
    nonigativetakengd: Optional[int]
    webpurifyresponse: str
    finalfxnewplayerid: int | None
    finalfxoldplayerid: int | None
    player_swap_details: int | None
    is_wildcard_taken_gd_id: int | None
    inactive_driver_penality_points: int | None


class CurrentUsersTeamsResponse(BaseModel):
    mdid: int | None
    userTeam: list[UserTeamItem]
    retval: int | None
