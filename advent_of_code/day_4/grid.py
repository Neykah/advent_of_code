from typing import Optional

import numpy as np


class Grid:
    def __init__(self, data: np.ndarray):
        self._data = data
        self._marked = np.zeros_like(data)
        self._latest_number: Optional[int] = None

    def check_new_number(self, new_number: int) -> bool:
        self._latest_number = new_number
        self._marked[self._data == new_number] = 1
        return (self._data == new_number).any()

    def check_victory(self) -> bool:
        return self._check_rows() or self._check_cols()

    def _check_rows(self) -> bool:
        return any(self._marked.min(axis=1) == 1)

    def _check_cols(self) -> bool:
        return any(self._marked.min(axis=0) == 1)

    def __getitem__(self, *args):
        return self._data.__getitem__(args)

    @property
    def _unmarked_sum(self) -> int:
        return (np.where(~self._marked, self._data, 0)).sum()

    @property
    def win_score(self) -> int:
        if self._latest_number is None:
            raise NotImplementedError
        return self._unmarked_sum * self._latest_number
