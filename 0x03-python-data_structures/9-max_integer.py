#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_value = my_ist[0]
        for num in my_list:
            if num > max_value:
                max_value = num
        return max_value
