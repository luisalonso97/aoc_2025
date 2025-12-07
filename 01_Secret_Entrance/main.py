import re
import utils.file_reader as fr


class Dial:
    def __init__(self, start_pos: int = 50, size: int = 100):
        self.position: int = start_pos
        self.size: int = size
        self.match_click: int = 0

    def rotate(self, direction: str, steps: int) -> None:
        if steps == 0:
            return

        self.match_click += steps // self.size

        remaining_steps: int = steps % self.size
        if remaining_steps == 0:
            return

        if direction == "R":
            if self.position + remaining_steps > self.size:
                self.match_click += 1

            self.position = (self.position + remaining_steps) % self.size

        elif direction == "L":
            if self.position - remaining_steps < 0 and self.position != 0:
                self.match_click += 1

            self.position = (self.position - remaining_steps) % self.size

        if self.position == 0:
            self.match_click += 1


def main() -> None:
    parse_exp: re.Pattern = re.compile(r"(R|L)([0-9]+)")
    data: list[re.Match] = fr.read_file("inputs/01.dat", parse_exp, re.match)

    dial: Dial = Dial()

    for move in data:
        direction: str = move.group(1)
        steps: int = int(move.group(2))
        dial.rotate(direction, steps)

    print(dial.match_click)


if __name__ == "__main__":
    main()
