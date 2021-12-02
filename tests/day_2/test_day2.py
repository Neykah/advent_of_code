from pathlib import Path

import pytest

import day_2.d2_scripts as d2

PLACEHOLDER_PATH = Path("tests/day_2/placeholder.txt")


@pytest.fixture
def instructions() -> list[d2.Instruction]:
    return d2.load_data(PLACEHOLDER_PATH)


def test_load_data(instructions):
    first_record: d2.Instruction = instructions[0]
    assert len(instructions) == 6
    assert len(first_record) == 2
    assert first_record.direction == "forward"
    assert first_record.intensity == 5


def test_sub_dive():
    sub = d2.Submarine()
    sub.dive(3)
    assert sub.depth == 3
    sub.dive(-1)
    assert sub.depth == 2


def test_sub_move():
    sub = d2.Submarine()
    sub.move_forward(3)
    assert sub.x_pos == 3


def test_follow_instruction_dive():
    sub = d2.Submarine()
    instruction = d2.Instruction("down", 5)
    sub.follow_instruction(instruction)
    assert sub.depth == 5
    assert sub.x_pos == 0


def test_follow_instruction_go_up():
    sub = d2.Submarine(depth=10)
    instruction = d2.Instruction("up", 2)
    sub.follow_instruction(instruction)
    assert sub.depth == 8
    assert sub.x_pos == 0


def test_follow_instruction_move():
    sub = d2.Submarine(depth=5)
    instruction = d2.Instruction("forward", 3)
    sub.follow_instruction(instruction)
    assert sub.depth == 5
    assert sub.x_pos == 3


def test_follow_all_instructions(instructions):
    sub = d2.Submarine()
    sub.follow_all_instructions(instructions)
    assert sub.x_pos == 15
    assert sub.depth == 10


def test_solve_p1(instructions):
    result = d2.solve_p1(instructions)
    assert result == 150


def test_solve_p2(instructions):
    result = d2.solve_p2(instructions)
    assert result == 900
