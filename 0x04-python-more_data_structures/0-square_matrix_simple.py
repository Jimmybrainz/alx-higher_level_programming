#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not all(isinstance(i, list) for i in matrix):
        raise ValueError("Input should be a 2D list")
    new_matrix = [[element**2 for element in row] for row in matrix]
    return new_matrix
