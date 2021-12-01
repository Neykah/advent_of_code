from pathlib import Path
import numpy as np

INPUT_PATH = Path("day_1/input.txt")


def count_nb_increase(input_data: list[int]) -> int:
    """Count the number of times an element in the input data has a higher value
    than the previous element
    """

    diff = compute_rolling_diff(input_data)
    result = np.count_nonzero(diff > 0)
    return result


def compute_rolling_diff(input_data: list[int]) -> np.ndarray:
    """Compute the difference between successive elements of the input iterable."""
    
    diff = []
    for i, d in enumerate(input_data):
        if i == 0:
            continue
        diff.append(d - input_data[i - 1])
    diff = np.array(diff)
    return diff


def sliding_sum(data: list[int], win_size: int = 3) -> np.ndarray:
    """Compute the sliding sum over a list of integer.

    The sliding sum is a list where each element is composed of the sum of {win_size}
    consecutive elements in the original iterable.
    """

    res = []
    for i, _ in enumerate(data):
        if i < win_size - 1:
            continue
        res.append(sum(data[i - win_size + 1 : i + 1]))
    return res


def load_data(input_path: Path) -> list[int]:
    """Extract data from an input text file."""

    with open(input_path, "r") as fp:
        input_data = [int(line.strip("\n")) for line in fp.readlines()]
    return input_data


solve_problem_1 = count_nb_increase


def solve_problem_2(input_data: list[int]) -> int:
    win_sum = sliding_sum(input_data)
    return count_nb_increase(win_sum)


if __name__ == "__main__":
    input_data = load_data(INPUT_PATH)

    result_1 = solve_problem_1(input_data)
    print("Result of problem 1:", result_1)

    result_2 = solve_problem_2(input_data)
    print("Result of problem 2:", result_2)
