#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not isinstance(a_dictionary, dict) or not isinstance(key, str):
        raise ValueError(
                "Input should be a dictionary and key should be a string")
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
