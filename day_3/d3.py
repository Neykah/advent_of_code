from pathlib import Path

import numpy as np

INPUT_PATH = Path("day_3/input.txt")


def calculate_gamma(arr: np.ndarray) -> int:
    majority = calculate_majority_value_in_cols(arr)
    majority = majority.astype(str).tolist()
    return int("".join(majority), base=2)


def calculate_majority_value_in_cols(arr):
    nb_lines = len(arr)
    col_sums = arr.sum(axis=0) / nb_lines
    majority = np.floor(col_sums + 0.5).astype(int)
    return majority


def calculate_epsilon(arr: np.ndarray) -> int:
    minority = 1 - calculate_majority_value_in_cols(arr)
    minority = minority.astype(str).tolist()
    return int("".join(minority), base=2)


def read_file(pth: Path) -> np.ndarray:
    with open(pth, "r") as fp:
        values = []
        for line in fp.readlines():
            line_elems = [bool(int(elem)) for elem in list(line.strip("\n"))]
            values.append(line_elems)

    arr = np.array(values, dtype=bool)
    return arr


def get_power_consumption(arr: np.ndarray) -> int:
    gamma = calculate_gamma(arr)
    epsilon = calculate_epsilon(arr)
    return gamma * epsilon


if __name__ == "__main__":
    arr = read_file(INPUT_PATH)
    print("Power consumption: ", get_power_consumption(arr))
