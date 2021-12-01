import day_1.d1_scripts as d1
from pathlib import Path
import pytest

PLACEHOLDER_PATH = Path("tests/day_1/placeholder.txt")


@pytest.fixture(scope="module")
def data():
    return d1.load_data(PLACEHOLDER_PATH)


def test_rolling_diff(data):
    diff = d1.compute_rolling_diff(data)
    assert len(diff) == len(data) - 1


def test_problem1(data):
    assert d1.solve_problem_1(data) == 7

def test_problem2(data):
    assert d1.solve_problem_2(data) == 5

def test_data_load(data):
    assert len(data) == 10

def test_sliding_sum(data):
    sliding_sum = d1.sliding_sum(data)
    assert len(sliding_sum) == len(data) - 2
    assert sliding_sum[1] > sliding_sum[0]
    assert sliding_sum[0] == 607
    assert sliding_sum[1] == 618
