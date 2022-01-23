from pathlib import Path
from typing import Optional

import numpy as np

from . import file_io as io
from .grid import Grid

INPUT_PATH = Path("advent_of_code/day_4/input.txt")


class GameMaster:
    def __init__(self, announcements: list[int], grid_arrays: list[np.ndarray]):
        self.future_announcements = announcements
        self.previous_announcements: list[int] = []
        self.player_grids = [Grid(grid) for grid in grid_arrays]

    def play_one_turn(self) -> Optional[Grid]:
        number = self.future_announcements.pop(0)
        self.previous_announcements.append(number)

        for i, player_grid in enumerate(self.player_grids):
            fit = player_grid.check_new_number(number)
            if fit:
                bingo = player_grid.check_victory()
                if bingo:
                    return self.player_grids[i]
        return None


def p1_get_winning_board(input_path: Path):
    announcements = io.get_announcements(input_path)
    boards = io.get_boards(input_path)
    winning_board = None

    game_master = GameMaster(announcements, boards)
    while winning_board is None:
        winning_board = game_master.play_one_turn()
    return winning_board


def main():
    winning_board = p1_get_winning_board(INPUT_PATH)
    print("Winning board score:", winning_board.win_score)
