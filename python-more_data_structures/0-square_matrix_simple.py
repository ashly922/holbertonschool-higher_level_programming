#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Create a new row to store the squared values
        squared_row = []

        # Iterate over each element in the row and square it
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)

        # Add the squared row to the result matrix
        result.append(squared_row)

    return result
