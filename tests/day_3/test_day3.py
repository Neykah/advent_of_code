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
