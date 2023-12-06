#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not isinstance(a_dictionary, dict):
        raise ValueError("Input should be a dictionary")
    new_dictionary = {key: 2 * value for key, value in a_dictionary.items()}
    return new_dictionary
