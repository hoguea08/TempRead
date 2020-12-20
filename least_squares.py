import matrix_multiplication

'''
This is the process that generates the least-squares approximation
formula for each core.
'''


def generate_least_squares(matrix_x, matrix_xt, matrix_y):
    """
    This calls the functions to perform Gaussian Elimination on
    two matrices to get the c_0 and c_1 coefficients to create the
    phi_hat global least-squares formula
    :param matrix_x: rhs matrix to XTX; contains time data
    :param matrix_xt: lhs matrix for XTX and XTY; transpose of X
    :param matrix_y: rhs matrix to XTY; contains temperature data
    :return: returns the phi_hat formula
    """
    xtx = matrix_multiplication.multiply(matrix_xt, matrix_x)
    xty = matrix_multiplication.multiply(matrix_xt, matrix_y)
    result = matrix_multiplication.augment_matrices(xtx, xty)

    # For each row in the augmented matrix, perform Gaussian
    # Elimination steps:
    # 1) Find largest row and swap
    # 2) Scale
    # 3) Eliminate
    for row in range(0, len(result[0])):
        if row != len(result[0]) - 1:
            index = matrix_multiplication.find_largest_row_by_col \
                (result, len(result) - 1, len(result[0]), row)
            matrix_multiplication.swap_row(result, row, index)
        matrix_multiplication.scale_row(result, row, len(result))
        result[row][row] = 1

        matrix_multiplication.eliminate(result, row, len(result))

        # Backsolve simplified matrix
    matrix_multiplication.back_solve(result)

    # Get the phi_hat approximation formula
    phi_hat = matrix_multiplication.get_phi_hat(result)
    return phi_hat
