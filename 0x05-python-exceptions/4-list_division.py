def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                division = element_1 / element_2
                result.append(division)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
