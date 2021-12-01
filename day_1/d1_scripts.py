from pathlib import Path
import numpy as np

INPUT_PATH = Path("day_1/input.txt")


def count_nb_increase(input_data: list[int]) -> int:
    diff = compute_rolling_diff(input_data)
    result = np.count_nonzero(diff >= 0)
    return result


def compute_rolling_diff(input_data: list[int]) -> np.ndarray:
    diff = []
    for i, d in enumerate(input_data):
        if i == 0:
            continue
        diff.append(d - input_data[i - 1])
    diff = np.array(diff)
    return diff


def load_data(input_path: Path) -> list[int]:
    with open(input_path, "r") as fp:
        input_data = [int(line.strip("\n")) for line in fp.readlines()]
    return input_data


solve_problem_1 = count_nb_increase

def solve_problem_2(input_data: list[int]) -> int:
    ...

if __name__ == "__main__":
    input_data = load_data(INPUT_PATH)

    result_1 = solve_problem_1(input_data)
    print("Result of problem 1:", result_1)

    result_2 = solve_problem_2(input_data)
