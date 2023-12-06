#!/usr/bin/python3
def number_keys(a_dictionary):
    if not isinstance(a_dictionary, dict):
        raise VauleError("Input should be a dictionary")
    num_keys = len(a_dictionary)
    return num_keys
