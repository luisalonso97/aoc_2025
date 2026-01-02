import re
import utils.file_reader as fr


def read_file(f_name: str) -> list[str]:
    with open(f_name, encoding="utf_8") as f:
        lines = [line.rstrip() for line in f]
    return lines


def check_battery_bound(batteries: list[int, int, int], battery_to_check: str) -> list[int, int, int]:
    pb, lb, rb = batteries
    btc: int = int(battery_to_check)

    # Check for the next biggest value
    if btc >= rb:
        rb = btc
    # If a bigger value is found save the previous value in the case no value
    # greater is bigger than the previous state.
    if lb < rb:
        pb = lb
        lb = rb
        rb = -1

    return [pb, lb, rb]


def main() -> None:
    banks: list[str] = read_file("inputs/03.dat")
    sum_of_max_batts: int = 0

    for bank in banks:
        batteries: list[int, int, int] = [-1, -1, -1]

        for bat in bank:
            batteries = check_battery_bound(batteries, bat)

        p, r, l = batteries
        # If one of the parts is -1 means no other pair was found
        bat0 = int(f"{p}{r}") if p > 0 and r > 0 else 0
        bat1 = int(f"{r}{l}") if r > 0 and l > 0 else 0

        sum_of_max_batts += max(bat0, bat1)

    print(sum_of_max_batts)


if __name__ == "__main__":
    main()

