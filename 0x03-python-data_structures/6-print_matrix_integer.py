#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        nr = len(matrix)
        nc = len(matrix[0])
        for i in range(nr):
            for j in range(nc):
                if j == nc - 1:
                    print('{:d}'.format(matrix[i][j]))
                else:
                    print('{:d} '.format(matrix[i][j]), end='')
    else:
        print()
