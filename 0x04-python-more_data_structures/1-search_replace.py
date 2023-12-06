#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not isinstance(my_list, list):
        raise ValueError("Input should be a list")
    new_list = [replace if element == search else element
                for element in my_list]
    return new_list
