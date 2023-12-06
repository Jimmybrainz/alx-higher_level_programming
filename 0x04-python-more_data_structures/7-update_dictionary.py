#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not isinstance(a_dictionary, dict) or not isinstance(key, str):
        raise ValueError(
            "Input should be a dictionary and key should be a string")
    a_dictionary[key] = value
    return a_dictionary
