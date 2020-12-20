'''
This is the process to create a piecewise linear interpolation for each core's
temperatures.
'''


def linear_interpolation(data, file, least_squares_form):
    """
    This calculates the linear interpolation for each set of points in the data.
    It then writes the least-squares formula and all of the linear interpolation
    formulas to a file.
    :param data: the temperature data matrix
    :param file: the file in which to write the formulas
    :param least_squares_form: the global least-squares approximation formula for the data
    :return: writes to a data file but does not return a value
    """
    least_squares_data = "{:>5} <= x < {:>7}; y_{:<6} = {:>7}; least-squares".format(str(0), str((len(data[0])-1) * 30),
                                                                                     'x', least_squares_form)
    file.write("%s\n" % least_squares_data)
    for i in range(len(data)):
        for value in range(0, len(data[0]) - 1):
            linear_function = create_line(value*30, (value + 1)*30, data[i][value], data[i][value + 1])
            file_data = ("{:>5} <= x < {:>7}; y_{:<6} = {:>7}; interpolation".format(value * 30,
                                                                                     (value + 1) * 30, value,
                                                                                     linear_function))
            file.write("%s\n" % file_data)
    file.close()


def create_line(x_0, x_1, y_0, y_1):
    """
    Creates the linear formula for each set of data points
    :param x_0: point 1 x-value
    :param x_1: point 2 x-value
    :param y_0: point 1 y-value
    :param y_1: point 2 y-value
    :return: returns a linear function in the form "b + mx," where
             b is the y-intercept and m is the slope
    """
    linear_function = ''

    slope = (y_1 - y_0) / (x_1 - x_0)
    intercept = y_0 - (slope * x_0)

    linear_function = "{:>12.4f} + {:>8.4f}x".format(intercept, slope)
    return linear_function
