import day_1.problem_1 as p1
from pathlib import Path
import pytest

PLACEHOLDER_PATH = Path("tests/day_1/placeholder.txt")


@pytest.fixture(scope="module")
def data():
    return p1.load_data(PLACEHOLDER_PATH)


def test_rolling_diff(data):
    diff = p1.compute_rolling_diff(data)
    assert len(diff) == len(data) - 1


def test_problem1(data):
    assert p1.count_nb_increase(data) == 7


def test_data_load(data):
    assert len(data) == 10
