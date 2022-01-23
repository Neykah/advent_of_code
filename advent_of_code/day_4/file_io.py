from pathlib import Path

import numpy as np


def get_lines(input_path: Path) -> list[str]:
    with open(input_path, "r") as fp:
        file_lines = [line.strip("\n") for line in fp.readlines()]
    return file_lines


def separate_announcements_from_boards(file_lines) -> tuple[list[int], list[str]]:
    announcement, boards = file_lines[0], file_lines[2:]
    announcement_list = [int(a) for a in announcement.split(",")]
    return announcement_list, boards


def create_board_arrays(board_strings: list[str]) -> list[np.ndarray]:
    all_boards = []
    current_board_data: list[list[int]] = []

    for line in board_strings:
        if not line:
            all_boards.append(np.array(current_board_data))
            current_board_data = []
            continue
        line_arr = [int(elem) for elem in line.split(" ") if elem]
        current_board_data.append(line_arr)

    all_boards.append(np.array(current_board_data, dtype=int))
    return all_boards


def get_announcements(input_path: Path) -> list[int]:
    file_lines = get_lines(input_path)
    announcements, _ = separate_announcements_from_boards(file_lines)
    return announcements


def get_boards(input_path: Path) -> list[np.ndarray]:
    file_lines = get_lines(input_path)
    _, board_strings = separate_announcements_from_boards(file_lines)
    boards_data = create_board_arrays(board_strings)
    return boards_data
