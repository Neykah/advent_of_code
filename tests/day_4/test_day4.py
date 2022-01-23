from pathlib import Path

import pytest

import advent_of_code.day_4.d4 as d4
import advent_of_code.day_4.file_io as io

INPUT_PATH = Path("tests/day_4/placeholder.txt")


@pytest.fixture
def game_master() -> d4.GameMaster:
    announcements = io.get_announcements(INPUT_PATH)
    boards = io.get_boards(INPUT_PATH)
    return d4.GameMaster(announcements, boards)


def test_winning_board():
    winning_board = d4.p1_get_winning_board(INPUT_PATH)
    assert winning_board[0][0] == 14


def test_first_announcement_value(game_master: d4.GameMaster):
    assert not game_master.previous_announcements
    game_master.play_one_turn()
    assert game_master.previous_announcements == [7]
