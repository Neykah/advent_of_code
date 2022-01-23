from pathlib import Path

import numpy as np
import pytest

from day_3 import d3

INPUT_PATH = Path("tests/day_3/placeholder.txt")


@pytest.fixture
def placeholder_data() -> np.ndarray:
    return d3.read_file(INPUT_PATH)


def test_read_columns(placeholder_data: np.ndarray):
    assert placeholder_data.shape[1] == 5
    assert np.array_equal(
        placeholder_data[:, 0],
        [
            False,
            True,
            True,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            False,
            False,
        ],
    )
    assert np.array_equal(
        placeholder_data[:, 1],
        [
            False,
            True,
            False,
            False,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
            True,
        ],
    )


def test_read_gamma(placeholder_data: np.ndarray):
    gamma = d3.calculate_gamma(placeholder_data)
    assert gamma == 22


def test_read_epsilon(placeholder_data: np.ndarray):
    epsilon = d3.calculate_epsilon(placeholder_data)
    assert epsilon == 9


def test_get_oxygen_generator_rating(placeholder_data: np.ndarray):
    oxygen_generator_rating = d3.get_oxygen_generator_rating(placeholder_data)
    assert oxygen_generator_rating == 23


def test_get_co2_scrubber_rating(placeholder_data: np.ndarray):
    co2_scrubber_rating = d3.get_co2_scrubber_rating(placeholder_data)
    assert co2_scrubber_rating == 10


def test_majority_0():
    data = np.array(
        [
            [0, 0, 1],
            [1, 1, 0],
            [0, 0, 0],
        ]
    )
    majority = d3.calculate_majority_value_in_cols(data)
    assert np.array_equal(majority, [0, 0, 0])


def test_majority_1():
    data = np.array(
        [
            [1, 0, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]
    )
    majority = d3.calculate_majority_value_in_cols(data)
    assert np.array_equal(majority, [1, 1, 1])


def test_ambiguous_majority_1():
    data = np.array(
        [
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
        ]
    )
    majority = d3.calculate_majority_value_in_cols(data, round_up=True)
    assert np.array_equal(majority, [1, 1, 1])


def test_ambiguous_majority_0():
    data = np.array(
        [
            [0, 0, 1],
            [1, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
        ]
    )
    majority = d3.calculate_majority_value_in_cols(data, round_up=False)
    assert np.array_equal(majority, [0, 0, 0])


def test_remove_2_rows_1st_position():
    data = np.array(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 0, 1],
        ]
    )
    filtered_arr = d3.remove_non_compliant_rows(data, 0, round_up=False)
    assert filtered_arr.shape == (2, 3)
    assert np.array_equal(filtered_arr, np.array([[0, 1, 0], [0, 0, 1]]))


def test_remove_2_rows_2nd_position():
    data = np.array(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 0, 1],
        ]
    )
    filtered_arr = d3.remove_non_compliant_rows(data, 1, round_up=False)
    assert filtered_arr.shape == (2, 3)
    assert np.array_equal(filtered_arr, np.array([[0, 0, 1], [1, 0, 1]]))
