#! /usr/bin/env python3

'''
This program contains a matrix multiplication algorithm,
and initializes three matrices: XT, X, and Y.
It multiples XT * X and XT * Y and prints the resulting
matrices.

'''
from typing import List


def create_matrix(num_rows, num_cols):
    """
    Creates the X matrix
    :param num_rows: number of rows in the matrix
    :param num_cols: number of columns in the matrix
    :return: returns the resulting matrix
    """
    X = [[0 for i in range(num_rows)] for j in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            if j == 0:
                X[j][i] = 1
            else:
                X[j][i] = i * 30
    return X


def create_transpose(num_rows, num_cols):
    """
    Creates the XT (transpose) matrix
    :param num_rows: number of rows in the matrix
    :param num_cols: number of columns in the matrix
    :return: returns the resulting matrix
    """
    XT = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            if j == 0:
                XT[i][j] = 1
            else:
                XT[i][j] = i * 30
    return XT


def multiply(lhs, rhs):
    '''
    multiply takes two matrices and performs matrix
    multiplication

    :param lhs: left-hand side matrix
    :param rhs: right-hand side matrix
    :return: result - the resulting matrix
    '''
    lhs_rows = len(lhs[0])
    lhs_columns = len(lhs)
    rhs_columns = len(rhs)
    result = [[0 for i in range(lhs_rows)] for j in range(rhs_columns)]

    for k in range(len(result)):
        for i in range(lhs_rows):
            for j in range(lhs_columns):
                result[k][i] += (lhs[j][i] * rhs[k][j])
    return result


def augment_matrices(matrix1, matrix2):
    '''
    Augments two matrices

    :param matrix1: the coefficient matrix
    :param matrix2: the constant matrix
    :return: augmented matrix (matrix 1 + matrix 2)
    '''
    return matrix1 + matrix2


def find_largest_row_by_col(matrix, col_index, num_rows, start_row_index):
    '''
    Given a column, finds the index of the row with the
    largest number

    :param matrix: augmented matrix to be analyzed
    :param col_index: column to be checked
    :param num_rows: number of rows in the column
    :param start_row_index: index of row to start checking
    :return: returns index of row with largest number
    '''
    max_value = 0
    for row in range(start_row_index, num_rows):
        max_value = max(max_value, matrix[col_index][row])
    for i in range(start_row_index, num_rows):
        index = matrix[col_index].index(max_value)
    return index


def swap_row(matrix, initial_row, largest_row_index):
    '''
    Swaps two rows in a matrix

    :param matrix: matrix with rows to be swapped
    :param initial_row: first row to be swapped
    :param largest_row_index: second row to be swapped
    :return: returns nothing
    '''
    for column in range(len(matrix)):
        temp = matrix[column][initial_row]
        matrix[column][initial_row] = matrix[column][largest_row_index]
        matrix[column][largest_row_index] = temp


def scale_row(matrix, row_index, num_columns):
    '''
    Scales the values of an entire row by the first
    number in that row

    :param matrix: matrix containing the row
    :param row_index: index of row to be scaled
    :param num_columns: number of columns in the row
    :return: returns nothing
    '''
    for column in range(0, num_columns):
        if matrix[column][row_index] != 0:
            scale = matrix[column][row_index]
            break

    for column in range(0, num_columns):
        matrix[column][row_index] *= 1 / scale


def eliminate(matrix, src_row_index, num_cols):
    '''
    eliminate a coefficient value by subtracting each value
    in a row by (its first value * the value in the first row and
    corresponding column)

    :param matrix: matrix containing row to be eliminated
    :param src_row_index: first row of matrix
    :param num_cols: number of columns in the row
    :param num_rows: number of rows
    :return: returns nothing
    '''
    start_col = matrix[0][src_row_index]
    value = 0

    for row in range(src_row_index + 1, len(matrix[0])):
        value = matrix[0][row]
        for column in range(0, num_cols):
            matrix[column][row] = matrix[column][row] - \
                                  value * matrix[column][src_row_index]
        matrix[0][row] = 0


def back_solve(matrix):
    '''
    backsolves the matrix for r0 = r0 - (first non-1 value in the row)*r1
    :param matrix: matrix to be backsolved
    :return: returns nothing
    '''
    augmented_index = len(matrix) - 1
    last_row = len(matrix[0]) - 1

    for i in range(last_row, 0, -1):
        for j in range(i - 1, -1, -1):
            s = matrix[i][j]

            matrix[i][j] -= (s * matrix[i][i])
            matrix[augmented_index][j] -= (s * matrix[augmented_index][i])


def get_phi_hat(matrix):
    '''
    assigns the values for the phi_hat formula coefficients,
    c_0, c_1, and c_2
    if a coefficient value is 0, does not print that term
    in the formula

    :param matrix: the augmented matrix with coefficient values
    :return: returns nothing
    '''
    last_row = len(matrix[0]) - 1

    if last_row == 2:
        c_0 = matrix[len(matrix) - 1][0]
        c_1 = matrix[len(matrix) - 1][1]
        c_2 = matrix[len(matrix) - 1][2]
    elif last_row == 1:
        c_0 = matrix[len(matrix) - 1][0]
        c_1 = matrix[len(matrix) - 1][1]
        c_2 = 0
    elif last_row == 0:
        c_0 = matrix[len(matrix) - 1][0]
        c_1 = 0
        c_2 = 0
    else:
        c_0 = c_1 = c_2 = 0

    phi_hat = ("{:>12.4f} + {:>8.4f}x".format(c_0, c_1))
    # phi_hat = str(c_0) + " + " + str(c_1) + " * x + " + str(c_2) + " * x^2"
    return phi_hat

def print_matrix(matrix):
    '''
    print_matrix prints a matrix to the screen

    :param matrix: the matrix vector to be printed
    :return: returns nothing
    '''
    for i in range(len(matrix[0])):
        print("|", end='')
        for j in range(len(matrix)):
            if matrix[j][i] != 0:
                print(" {:<} ".format(matrix[j][i]), end='')
            else:
                print(" {:<} ".format(abs(matrix[j][i])), end='')
        print("|")
