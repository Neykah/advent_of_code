from pathlib import Path

import day_4.file_io as file_io
import numpy as np
import pytest

INPUT_PATH = Path("tests/day_4/placeholder.txt")


@pytest.fixture
def announcements() -> list[int]:
    lines = file_io.get_lines(INPUT_PATH)
    announcements, _ = file_io.separate_announcements_from_boards(lines)
    return announcements


@pytest.fixture
def boards() -> list[np.ndarray]:
    lines = file_io.get_lines(INPUT_PATH)
    _, board_strings = file_io.separate_announcements_from_boards(lines)
    return file_io.create_board_arrays(board_strings)


def test_get_lines():
    lines = file_io.get_lines(INPUT_PATH)
    assert len(lines) == 19


def test_announcement_is_list(announcements: list[int]):
    assert isinstance(announcements, list)


def test_announcement_1st_val(announcements: list[int]):
    assert announcements[0] == 7


def test_announcement_type(announcements: list[int]):
    assert all([isinstance(a, int) for a in announcements])


def test_announcement_len(announcements: list[int]):
    assert len(announcements) == 27


def test_3_boards(boards: list[np.ndarray]):
    assert len(boards) == 3


def test_board_shape(boards: list[np.ndarray]):
    assert boards[0].shape == (5, 5)


def test_first_board_values(boards: list[np.ndarray]):
    np.testing.assert_array_equal(
        boards[0],
        np.array(
            [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ]
        ),
    )
