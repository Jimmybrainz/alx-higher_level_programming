#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not isinstance(my_list, list):
        raise ValueError("Input should be a list")
    unique_set = set(my_list)
    sum_unique = sum(unique_set)
    return sum_unique
