#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        raise ValueError("Input should be sets")
    common_set = set_1 & set_2
    return common_set
