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


if __name__ == "__main__":
    input_data = load_data(INPUT_PATH)
    result = count_nb_increase(input_data)
    print(result)
