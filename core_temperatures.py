#! /usr/bin/env python3

"""
This is the main function for determining a global least-squares approximation
formula and piecewise linear interpolation for four sets of CPU core temperatures
"""

import sys
import matrix_multiplication
import least_squares
import interpolation
from parse_temps import (parse_raw_temps)


def main():
    """
    This is the main function for setting up the data for the four CPU cores and
    calling the least-squares and interpolation calculators
    :return: does not return a value, but four data files are created - one for
             each CPU core
    """
    if len(sys.argv) < 2:
        sys.exit("You did not provide any input data:\n"
                 "Usage: python3 core_temperatures.py {input_file.txt}")
    input_temps = sys.argv[1]
    basename = input_temps.split('.')
    new_list = []

    # Read the input data file and create a list of tuples
    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            new_list.append(temps_as_floats)

    # Create an X and XT matrix using the length of input data
    num_rows = len(new_list)
    num_cols = len(new_list[0])
    x = matrix_multiplication.create_matrix(num_rows, num_cols)
    xt = matrix_multiplication.create_transpose(num_rows, num_cols)

    # Initialize Y matrices for each CPU core
    core_1_y = [[0 for i in range(len(new_list))] for j in range(1)]
    core_2_y = [[0 for i in range(len(new_list))] for j in range(1)]
    core_3_y = [[0 for i in range(len(new_list))] for j in range(1)]
    core_4_y = [[0 for i in range(len(new_list))] for j in range(1)]

    # Build the Y matrices by inputting the corresponding core's temperatures
    for i in range(len(new_list)):
        core_1_y[0][i] = new_list[i][1][0]
        core_2_y[0][i] = new_list[i][1][1]
        core_3_y[0][i] = new_list[i][1][2]
        core_4_y[0][i] = new_list[i][1][3]

    # Generate the least-squares approximation formula for each core
    formula_1 = least_squares.generate_least_squares(x, xt, core_1_y)
    formula_2 = least_squares.generate_least_squares(x, xt, core_2_y)
    formula_3 = least_squares.generate_least_squares(x, xt, core_3_y)
    formula_4 = least_squares.generate_least_squares(x, xt, core_4_y)

    # Create a file for each core, calculate the piecewise linear
    # interpolation, and write both the least-squares and piecewise
    # linear interpolation formulas to the file
    file1 = open(basename[0] + "-core-1.txt", "w+")
    interpolation.linear_interpolation(core_1_y, file1, formula_1)

    file2 = open(basename[0] + "-core-2.txt", "w+")
    interpolation.linear_interpolation(core_2_y, file2, formula_2)

    file3 = open(basename[0] + "-core-3.txt", "w+")
    interpolation.linear_interpolation(core_3_y, file3, formula_3)

    file4 = open(basename[0] + "-core-4.txt", "w+")
    interpolation.linear_interpolation(core_4_y, file4, formula_4)


if __name__ == "__main__":
    main()
