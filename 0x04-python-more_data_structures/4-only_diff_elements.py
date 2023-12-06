#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        raise ValueError("Input should be sets")
    diff_set = set_1 ^ set_2
    return diff_set
