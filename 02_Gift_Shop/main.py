import re
import utils.file_reader as fr


def generate_invalid_ids(max_val: int) -> set[int]:
    invalid_ids = set()
    max_digits = len(str(max_val))

    for pattern_len in range(1, max_digits // 2 + 1):
        start_pat = 10 ** (pattern_len - 1)
        end_pat = 10 ** pattern_len

        for pat in range(start_pat, end_pat):
            pat_str = str(pat)

            current_str = pat_str * 2
            while len(current_str) <= max_digits:
                val = int(current_str)
                if val <= max_val:
                    invalid_ids.add(val)
                current_str += pat_str

    return invalid_ids


def main() -> None:
    parse_exp: re.Pattern = re.compile(r"(\d+)-(\d+)(?:,?)")
    data: list[list[tuple[str, str]]] = fr.read_file(
        "inputs/02.dat", parse_exp, re.findall
    )

    ranges: list[tuple[int, int]] = []
    max_id_needed: int = 0

    for match in data[0]:
        start = int(match[0])
        end = int(match[1])
        ranges.append((start, end))
        max_id_needed = max(max_id_needed, end)

    invalid_ids = generate_invalid_ids(max_id_needed)

    sum_of_invalid_ids: int = 0

    sorted_invalid_ids = sorted(list(invalid_ids))

    for val in sorted_invalid_ids:
        for start, end in ranges:
            if start <= val < end:
                sum_of_invalid_ids += val
                break

    print(sum_of_invalid_ids)


if __name__ == "__main__":
    main()
