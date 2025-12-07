from dataclasses import dataclass
import re

import utils.file_reader as fr


@dataclass
class IdRange:
    min_count: int
    max_count: int


def is_id_pattern_valid(id: str) -> bool:
    return id[: len(id) // 2] != id[len(id) // 2 :]


def main() -> None:
    parse_exp: re.Pattern = re.compile(r"(\d+)-(\d+)(?:,?)")
    data: list[list[tuple[str, str]]] = fr.read_file(
        "inputs/02.dat", parse_exp, re.findall
    )

    sum_of_invalid_ids: int = 0

    for match in data[0]:
        id_range: IdRange = IdRange(int(match[0]), int(match[1]))
        ids = (x for x in range(id_range.min_count, id_range.max_count))
        for id in ids:
            if not is_id_pattern_valid(str(id)):
                sum_of_invalid_ids += id

    print(sum_of_invalid_ids)


if __name__ == "__main__":
    main()
