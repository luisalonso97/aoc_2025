import re

import utils.file_reader as fr

MOVEMENTS: dict[str, int] = {
    "R": 1,
    "L": -1,
}


def apply_movement(inital_pos: int, direction: str, steps: int) -> int:
    return (inital_pos + (MOVEMENTS[direction] * steps)) % 100


def main() -> None:
    parse_exp: re.Pattern = re.compile(r"(R|L)([0-9]+)")
    # data: list[re.Match] = fr.read_file("inputs/01_trunc.dat", parse_exp, re.match)
    data: list[re.Match] = fr.read_file("inputs/01.dat", parse_exp, re.match)

    movements: list[tuple[str, int]] = [
        (move.group(1), int(move.group(2))) for move in data
    ]

    current_position: int = 50
    match_click: int = 0

    for movement in movements:
        if movement[1] == 0:
            continue

        # Get all full rotations
        full_rotations = movement[1] // 100
        match_click += full_rotations

        # Calculate remaining steps
        remaining_steps = movement[1] % 100

        # Check for pass
        if remaining_steps == 0:
            continue

        # Check if applying movement will pass the edge
        if movement[0] == "R" and current_position + remaining_steps > 100:
            match_click += 1
            # Apply movement
            current_position = apply_movement(
                current_position, movement[0], remaining_steps
            )
            continue
        elif (
            movement[0] == "L"
            and current_position - remaining_steps < 0
            and current_position != 0
        ):
            match_click += 1
            # Apply movement
            current_position = apply_movement(
                current_position, movement[0], remaining_steps
            )
            continue

        # Apply movement
        current_position = apply_movement(
            current_position, movement[0], remaining_steps
        )

        # Check for land
        if current_position == 0 or current_position == 100:
            match_click += 1

        if current_position == 100:
            current_position = 0

    print(match_click)  # 5892


if __name__ == "__main__":
    main()
