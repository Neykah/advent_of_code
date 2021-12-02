from collections import namedtuple
from pathlib import Path

Instruction = namedtuple("Instruction", ["direction", "intensity"])

INPUT_PATH = Path("day_2/input.txt")


class Submarine:
    def __init__(self, x_pos: int = 0, depth: int = 0) -> None:
        self.x_pos = x_pos
        self.depth = depth

    def dive(self, depth_delta: int) -> None:
        self.depth += depth_delta

    def move_forward(self, distance: int) -> None:
        self.x_pos += distance

    def follow_instruction(self, instruction: Instruction) -> None:
        func_map = {
            "forward": self.move_forward,
            "down": self.dive,
            "up": lambda x: self.dive(-x),
        }
        func_map[instruction.direction](instruction.intensity)

    def follow_all_instructions(self, instructions: list[Instruction]) -> None:
        for instruction in instructions:
            self.follow_instruction(instruction)


class ComplexSubmarine(Submarine):
    def __init__(self, x_pos: int = 0, depth: int = 0, aim: int = 0) -> None:
        super().__init__(x_pos, depth)
        self.aim = aim

    def process_down(self, intensity: int) -> None:
        self.aim += intensity

    def process_forward(self, intensity: int) -> None:
        self.move_forward(intensity)
        self.dive(self.aim * intensity)

    def follow_instruction(self, instruction: Instruction) -> None:
        func_map = {
            "forward": self.process_forward,
            "down": self.process_down,
            "up": lambda x: self.process_down(-x),
        }
        func_map[instruction.direction](instruction.intensity)


def load_data(input_path: Path) -> list[Instruction]:
    def extract_instruction(line: str) -> Instruction:
        direction, intensity = line.strip("\n").split(" ")
        return Instruction(direction=direction, intensity=int(intensity))

    with open(input_path, "r") as fp:
        return [extract_instruction(line) for line in fp.readlines()]


def make_sub_follow(sub: Submarine, instructions: list[Instruction]) -> int:
    sub.follow_all_instructions(instructions)
    res = sub.x_pos * sub.depth
    return res


def solve_p1(instructions: list[Instruction]):
    sub = Submarine()
    return make_sub_follow(sub, instructions)


def solve_p2(instructions: list[Instruction]):
    sub = ComplexSubmarine()
    return make_sub_follow(sub, instructions)


if __name__ == "__main__":
    instructions = load_data(INPUT_PATH)
    result_1 = solve_p1(instructions)
    print("Result of problem 1:", result_1)
    result_2 = solve_p2(instructions)
    print("Result of problem 1:", result_2)
