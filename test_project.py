import pytest
from tabulate import tabulate
from project import (
    calc_score,
    validate_choice,
    show_game_table,
    validate_season,
    seasons,
)


def test_calc_score():
    assert (
        calc_score(31.6, 81, 10.7, 10.4, 1.6, 0.4, 2.5, 0.425, 0.845, 34.6, 5.4)
        == 60.219133
    )


def test_validate_season_true():
    assert validate_season("2022-23") == True
    assert validate_season("2014-15") == True
    assert validate_season("2013-14") == True


def test_validate_season_false():
    assert validate_season("2014-16") == False
    assert validate_season("abcd") == False
    assert validate_season("2015,16") == False
    assert validate_season("2015_16") == False


def test_validate_choice():
    assert validate_choice("1") == True
    assert validate_choice("2") == True
    assert validate_choice("a") == False
    assert validate_choice("4") == False


def test_show_game_table():
    assert show_game_table(
        [[1, "Guess The MVP"], [2, "NBA Statistical Trends"]], ["SNo", "Choice"]
    ) == tabulate(
        [[1, "Guess The MVP"], [2, "NBA Statistical Trends"]],
        ["SNo", "Choice"],
        tablefmt="heavy_grid",
    )
