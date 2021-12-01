import day_1.d1_scripts as d1
from pathlib import Path
import pytest

PLACEHOLDER_PATH = Path("tests/day_1/placeholder.txt")


@pytest.fixture(scope="module")
def data():
    """Example data given during the challenge."""

    return d1.load_data(PLACEHOLDER_PATH)


def test_rolling_diff(data):
    """Sanity check on the rolling diff function."""

    diff = d1.compute_rolling_diff(data)
    assert len(diff) == len(data) - 1
    assert diff[0] == data[1] - data[0]


def test_problem1(data):
    """Solution to the example of problem 1."""

    assert d1.solve_problem_1(data) == 7


def test_problem2(data):
    """Solution to the example of problem 2."""

    assert d1.solve_problem_2(data) == 5


def test_data_load(data):
    """Sanity check on the data loader."""

    assert len(data) == 10


def test_sliding_sum(data):
    """Sanity check on the sliding sum function."""

    sliding_sum = d1.sliding_sum(data)
    assert len(sliding_sum) == len(data) - 2
    assert sliding_sum[1] > sliding_sum[0]
    assert sliding_sum[0] == 607
    assert sliding_sum[1] == 618
