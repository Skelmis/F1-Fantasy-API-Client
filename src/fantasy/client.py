from __future__ import annotations

import typing

import commons

from fantasy import models
from fantasy.api_models.drivers_and_constructors import ConstructorOrDriverItem
from fantasy.api_models.list_user_teams import UserTeamItem
from fantasy.models import leagues

if typing.TYPE_CHECKING:
    from fantasy import APIClient


class Client:
    def __init__(self, api_client: APIClient):
        self.api: APIClient = api_client

    @staticmethod
    def to_float(value: typing.Any) -> float:
        """Helper function for string transforms"""
        try:
            return float(value)
        except:
            return 0.0

    @staticmethod
    def to_int(value: typing.Any) -> int:
        """Helper function for string transforms"""
        try:
            return int(value)
        except:
            return 0

    async def get_private_league_leaderboard(
        self, league_id: int
    ) -> leagues.PrivateLeaderboard:
        """Fetch the leaderboard for your league!

        Parameters
        ----------
        league_id: int
            The league id we want a leaderboard for.

        Returns
        -------
        models.PrivateLeaderboard
        """
        raw_data = await self.api.get_private_leaderboard(league_id)
        entrants: list[leagues.PrivateLeaderboardEntrant] = []
        for member in raw_data.memRank:
            entrants.append(
                leagues.PrivateLeaderboardEntrant(
                    team_id=member.teamId,
                    team_number=member.teamNo,
                    team_name=member.teamName,
                    user_name=member.userName,
                    is_league_admin=commons.value_to_bool(member.isAdmin),
                    overall_points=member.total_current_points,
                    rank_in_league=member.rank,
                    guid=member.guid,
                )
            )

        return leagues.PrivateLeaderboard(
            members=entrants,
            league_id=league_id,
            league_member_count=(
                self.to_int(raw_data.leagueInfo.memCount)
                if raw_data.leagueInfo.memCount
                else None
            ),
            league_invite_code=raw_data.leagueInfo.leagueCode,
            league_name=raw_data.leagueInfo.leagueName,
        )

    async def get_user_leagues(self) -> leagues.UserLeagues:
        """Fetch the various user leagues you are a part of.

        Notes
        -----
        Does not appear to include public leagues.

        Returns
        -------
        leagues.UserLeagues
        """
        raw_data = await self.api.get_user_leagues()
        data: list[leagues.UserLeaguesEntrant] = []
        for league in raw_data.leaguesdata:
            teams_in_league: list[leagues.UserLeagueTeam] = []
            for team in league.teamInfo:
                teams_in_league.append(
                    leagues.UserLeagueTeam(
                        team_number=team.teamNo,
                        rank_in_league=team.userRank,
                    )
                )

            data.append(
                leagues.UserLeaguesEntrant(
                    league_id=league.leagueId,
                    league_invite_code=league.leagueCode,
                    league_name=league.leagueName,
                    league_type=league.leagueType,
                    is_league_admin=commons.value_to_bool(league.leagueAdmin),
                    member_count=(
                        self.to_int(league.memeberCount)
                        if league.memeberCount
                        else None
                    ),
                    league_vip_flag=league.legaueVipFlag,
                    teams_in_league=teams_in_league,
                )
            )

        return leagues.UserLeagues(
            leagues=data,
            total_count=raw_data.leaguestotcnt,
            vip_count=raw_data.leaguesvipcnt,
            classic_leagues_count=raw_data.leaguesclassiccnt,
        )

    async def fetch_constructors_and_drivers(
        self, race_id: int
    ) -> list[models.Driver | models.Constructor]:
        """Fetch all drivers and constructors for a given race.

        Parameters
        ----------
        race_id: int
            The race ID to get the drivers and constructors for.

            1 indexed from the start of the year.

            To get the current race id, call api.get_current_race_id()

        Returns
        -------
        list[models.Driver| models.Constructor]
        """
        data: list[models.Driver | models.Constructor] = []
        raw_data = await self.api.get_drivers_and_constructors(race_id)
        for entry in raw_data.data:
            entry = typing.cast(ConstructorOrDriverItem, entry)
            if entry.PositionName == "DRIVER":
                data.append(
                    models.Driver(
                        skill=entry.Skill,
                        value=entry.Value,
                        full_name=entry.FUllName,
                        display_name=entry.DisplayName,
                        team_name=entry.TeamName,
                        status=entry.Status,
                        is_active=commons.value_to_bool(entry.IsActive),
                        driver_tla=entry.DriverTLA,
                        driver_reference=entry.DriverReference,
                        country_name=entry.CountryName,
                        overall_points=self.to_float(entry.OverallPpints),
                        points_in_this_race=self.to_float(entry.GamedayPoints),
                        percentage_selected=self.to_float(entry.SelectedPercentage),
                        percentage_as_2x=self.to_float(entry.CaptainSelectedPercentage),
                        best_race_finish=self.to_int(entry.BestRaceFinished),
                        highest_grid_start=self.to_int(entry.HigestGridStart),
                        qualy_points=self.to_float(entry.QualifyingPoints),
                        race_points=self.to_float(entry.RacePoints),
                        sprint_points=self.to_float(entry.SprintPoints),
                        no_negative_points=self.to_float(entry.NoNegativePoints),
                        f1_player_id=entry.F1PlayerId,
                        player_id=entry.PlayerId,
                        first_name=entry.FirstName,
                        last_name=entry.LastName,
                        fastest_lap_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        driver_of_the_day_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        overtaking_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        q3_finishes_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        top_10_race_positions_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        top_8_sprint_positions_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        total_position_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        total_position_gained_lost=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        total_dnf_dq_points=(
                            self.to_float(entry.AdditionalStats.fastest_lap_pts)
                            if entry.AdditionalStats
                            else None
                        ),
                        value_for_money=(
                            self.to_float(entry.AdditionalStats.value_for_money)
                            if entry.AdditionalStats
                            else None
                        ),
                        raw_api_model=entry,
                    )
                )
            elif entry.PositionName == "CONSTRUCTOR":
                data.append(
                    models.Constructor(
                        skill=entry.Skill,
                        value=entry.Value,
                        full_name=entry.FUllName,
                        display_name=entry.DisplayName,
                        team_name=entry.TeamName,
                        overall_points=self.to_float(entry.OverallPpints),
                        points_in_this_race=self.to_float(entry.GamedayPoints),
                        percentage_selected=self.to_float(entry.SelectedPercentage),
                        percentage_as_2x=self.to_float(entry.CaptainSelectedPercentage),
                        best_race_finish=self.to_int(entry.BestRaceFinished),
                        highest_grid_start=self.to_int(entry.HigestGridStart),
                        qualy_points=self.to_float(entry.QualifyingPoints),
                        race_points=self.to_float(entry.RacePoints),
                        sprint_points=self.to_float(entry.SprintPoints),
                        no_negative_points=self.to_float(entry.NoNegativePoints),
                        f1_player_id=entry.F1PlayerId,
                        player_id=entry.PlayerId,
                        first_name=entry.FirstName,
                        last_name=entry.LastName,
                        fastest_lap_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        driver_of_the_day_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        overtaking_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        q3_finishes_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        top_10_race_positions_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        top_8_sprint_positions_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        total_position_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        total_position_gained_lost=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        total_dnf_dq_points=self.to_float(
                            entry.AdditionalStats.fastest_lap_pts
                        ),
                        value_for_money=self.to_float(
                            entry.AdditionalStats.value_for_money
                        ),
                        raw_api_model=entry,
                    )
                )
            else:
                raise ValueError(f"Unexpected value for {entry.PositionName}")

        return data

    async def fetch_team_info(self, team_id: str, race_id: int) -> leagues.LeagueTeam:
        """Fetch a team that's in a shared league.

        Parameters
        ----------
        team_id: str
            The team to lookup
        race_id: int
            The race ID to get the drivers and constructors for.

            1 indexed from the start of the year.

            To get the current race id, call api.get_current_race_id()

        Returns
        -------
        leagues.LeagueTeam
        """
        raw_data = await self.api.fetch_team_in_private_league(team_id, race_id)
        user_team: UserTeamItem = raw_data.userTeam[0]
        drivers_and_constructors = await self.fetch_constructors_and_drivers(race_id)
        raw_team_entries: list[leagues.TeamEntry] = [
            leagues.TeamEntry(
                id=entry.id,
                has_2x=commons.value_to_bool(entry.iscaptain),
                has_3x=commons.value_to_bool(entry.ismgcaptain),
            )
            for entry in user_team.playerid
        ]
        drivers: dict[str, models.Driver] = {
            d.player_id: d
            for d in drivers_and_constructors
            if isinstance(d, models.Driver)
        }
        constructors: dict[str, models.Constructor] = {
            d.player_id: d
            for d in drivers_and_constructors
            if isinstance(d, models.Constructor)
        }

        has_drivers = [drivers[i.id] for i in raw_team_entries if i.id in drivers]
        has_constructors = [
            constructors[i.id] for i in raw_team_entries if i.id in constructors
        ]

        return leagues.LeagueTeam(
            drivers=has_drivers,
            constructors=has_constructors,
            raw_team_entries=raw_team_entries,
            global_league_rank=self.to_int(user_team.ovrank),
            points_from_this_race=self.to_float(user_team.gdpoints),
            overall_points=self.to_float(user_team.ovpoints),
            team_name=user_team.teamname,
            current_booster=user_team.boosterid,
            is_using_wild_card=commons.value_to_bool(user_team.iswildcard),
            subs_allowed=user_team.subsallowed,
            user_subs_left=user_team.usersubsleft,
            extra_subs_cost=user_team.extrasubscost,
            raw_api_model=raw_data,
        )
