"""
Advent of Code 2021 - Day 3
Problem link: https://adventofcode.com/2021/day/3
"""

from pathlib import Path

import numpy as np

INPUT_PATH = Path("day_3/input.txt")


def calculate_gamma(arr: np.ndarray) -> int:
    majority = calculate_majority_value_in_cols(arr)
    return _convert_bin_array_to_int(majority)


def _convert_bin_array_to_int(bin_array: np.ndarray) -> int:
    bin_array = bin_array.astype(str).tolist()
    return int("".join(bin_array), base=2)


def calculate_majority_value_in_cols(
    arr: np.ndarray, round_up: bool = True
) -> np.ndarray:
    """For each column of the input binary array, computes the majority value (0 or 1).
    In case of equal number of occurrences of 0 and 1 in a column,
    returns float(round_up).

    Args:
        arr (np.ndarray): Binary array (all values are either 0 or 1)
        round_up (bool, optional): Whether to return 0 or 1 for a column in case of
        equal occurrences of 0 and 1. Defaults to True.

    Returns:
        np.ndarray: An array of shape (1, C), where C is the number of columns in arr.
        Each value describes the majority value in each of the columns of arr.
    """
    col_sums = np.mean(arr, axis=0)
    # Converts boolean to +- 0.01
    round_factor = ((float(round_up) * 2) - 1) / 100
    majority = np.floor(col_sums + 0.5 + round_factor).astype(int)
    return majority


def calculate_epsilon(arr: np.ndarray) -> int:
    minority = 1 - calculate_majority_value_in_cols(arr)
    return _convert_bin_array_to_int(minority)


def read_file(pth: Path) -> np.ndarray:
    with open(pth, "r") as fp:
        values = []
        for line in fp.readlines():
            line_elems = [bool(int(elem)) for elem in list(line.strip("\n"))]
            values.append(line_elems)

    arr = np.array(values, dtype=bool)
    return arr


def _core_lookup_logic(arr: np.ndarray, majority: bool) -> int:
    col_idx = 0
    while len(arr) > 1:
        arr = remove_non_compliant_rows(arr, col_idx, majority=majority)
        col_idx += 1
    bin_array = arr[0].astype(int)
    return _convert_bin_array_to_int(bin_array)


def get_oxygen_generator_rating(arr: np.ndarray) -> int:
    return _core_lookup_logic(arr, majority=True)


def get_co2_scrubber_rating(arr: np.ndarray) -> int:
    return _core_lookup_logic(arr, majority=False)


def remove_non_compliant_rows(
    arr: np.ndarray, col_nb: int, majority: bool
) -> np.ndarray:
    """Remove rows from the input array that do not have the majority value in their
    `col_nb`th column.

    Args:
        arr (np.ndarray): Input binary array of shape (N, M)
        col_nb (int): Column to use to consider whether the row should be removed.
            Must be < M.
        majority (bool): Whether or not the majority value (True) or the minority value
            (False) should be used in the bit criteria.

    Returns:
        np.ndarray: Binary array of shape (<= N, M).
    """
    if majority:
        cols_criteria = calculate_majority_value_in_cols(arr, round_up=True)
    else:
        cols_criteria = 1 - calculate_majority_value_in_cols(arr, round_up=True)
    rows_to_delete = []
    for row, val in enumerate(arr[:, col_nb]):
        if val != cols_criteria[col_nb]:
            rows_to_delete.append(row)

    arr = np.delete(arr, rows_to_delete, 0)

    return arr


def p1_get_power_consumption(arr: np.ndarray) -> int:
    gamma = calculate_gamma(arr)
    epsilon = calculate_epsilon(arr)
    return gamma * epsilon


if __name__ == "__main__":
    arr = read_file(INPUT_PATH)
    print("Power consumption: ", p1_get_power_consumption(arr))
