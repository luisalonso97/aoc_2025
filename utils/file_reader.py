"""
Helper to read puzzle data
"""

import re
import functools as ft


def read_file(f_name, parse_exp=None, match_f=None):
    with open(f_name, encoding="utf_8") as f:
        lines = [line.rstrip() for line in f]
    if parse_exp:
        mf = (
            ft.partial(match_f, parse_exp)
            if match_f
            else ft.partial(re.match, parse_exp)
        )
        lines = list(map(mf, lines))
    return lines
