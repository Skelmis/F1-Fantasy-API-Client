from pydantic import BaseModel

from fantasy.api_models.drivers_and_constructors import ConstructorOrDriverItem


class Base(BaseModel):
    skill: int
    value: float
    full_name: str
    display_name: str
    team_name: str
    overall_points: float
    points_in_this_race: float
    percentage_selected: float
    percentage_as_2x: float
    best_race_finish: int
    highest_grid_start: int
    qualy_points: float
    race_points: float
    sprint_points: float
    no_negative_points: float
    f1_player_id: str
    first_name: str
    last_name: str
    fastest_lap_points: float | None
    driver_of_the_day_points: float | None
    overtaking_points: float | None
    q3_finishes_points: float | None
    top_10_race_positions_points: float | None
    top_8_sprint_positions_points: float | None
    total_position_points: float | None
    total_position_gained_lost: float | None
    total_dnf_dq_points: float | None
    value_for_money: float | None
    raw_api_model: ConstructorOrDriverItem


class Driver(Base):
    status: str
    is_active: bool
    driver_tla: str
    driver_reference: str
    country_name: str


class Constructor(Base):
    pass
