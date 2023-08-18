def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [i ** 2 for i in row]
        squared_matrix.append(squared_row)
    return squared_matrix
