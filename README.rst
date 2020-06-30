*********
Linsolver
*********

Linsolver is a toy package for solving linear systems of equations Ax=b.


Prerequisites
=============

Linsolver needs Python 3 (version 3.5 or above) and the SciPy and NumPy
packages.


Creating the input
==================

Create an input file `linsolve.in` containing the coefficient matrix. Each
matrix row should be written in a separate line. The coefficient matrix
should be followed by the right-hand-side vector(s) b. Each b-vector
(column vector in the equation) should be written as a row vector in a
separate line. An example input with a 3x3 coefficient matrix and two
b-vectors could look like::

  # Coefficient matrix
  2.0  4.0  4.0
  1.0  2.0 -1.0
  5.0  4.0  2.0
  # RHS vectors as row vectors
  1.0  2.0  4.0
  2.0  6.0 -1.0

Comments line can be introduced by putting a hashmark (``#``) to the front.


Running the program
===================

Execute the `linsolve` script in the folder with the input file `linsolve.in`::

  linsolve

If the input file is located in an other directory, you may specify the folder
using the ``-d`` option::

  linsolve -d somedir

The output will be always written into the same folder as the input.


Interpreting the result
=======================

The result is written into the output file `linsolve.out`. It contains the
solution vectors x as row vector. For the example above, the output file would
look as::

  6.666666666666666297e-01 4.166666666666666852e-01 -5.000000000000000000e-01
  -2.111111111111111605e+00 3.222222222222222765e+00 -1.666666666666666741e+00


Useful tools
============

The linsolver package contains an additional tool `geninput` which can be used
to generate random input file for `linsolve`. Type ::

  geninput -h

to get an overview about the command line parameters.
