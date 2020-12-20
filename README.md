# TempRead

A Python program to take in CPU temperature data and output a piecewise linear interpolation and a global linear least squares approximation.

# Requirements

  * Python 3.6 or higher
  
  * Imports:
		matrix_multiplication.py
		least_squares.py
		interpolation.py
		parse_temps.py

# Sample Execution & Output
------------------------------------------------------------------------

If run without command line arguments, using

```
python3 core_temperatures.py
```

the following message will be displayed.

```
"You did not provide any input data:
Usage: python3 core_temperatures.py {input_file.txt}"

```

If run using an "input.txt" file:

```
python3 core_temperatures.py input.txt
```

the output will be four data text files that are generated in the form: 

{basename}-core-0.{txt}
{basename}-core-1.{txt}
{basename}-core-2.{txt}
{basename}-core-3.{txt}

The files will contain data in the form:

	x_k <= x < x_k+1; y_i = c0 + c1x ; type

where: 

	-x_k and x_k+1 are the domain in which y_i is applicable
	-y_i is the ith function
	-type is either least-squares or interpolation

-----------------------------------------------------------------------------
