#!/usr/bin/env python3
"""Contains routines to test the solvers module"""

import os.path
import pytest
import numpy as np
import numpy.linalg as linalg
import solvers
import linsolveio as io


ABSOLUTE_TOLERANCE = 1e-10
RELATIVE_TOLERANCE = 1e-10

TESTDATADIR = 'testdata'

TESTS = ['simple', 'needs_pivot', 'linearly_dependant', 'multiple']


def get_test_input(testname):
    "Reads the input for a given test."
    testinfile = os.path.join(TESTDATADIR, testname + '.in')
    aa, bb = io.read_input(testinfile)
    return aa, bb


def get_test_output(testname):
    "Reads the reference ouput for a given test."
    testoutfile = os.path.join(TESTDATADIR, testname + '.out')
    result = io.read_result(testoutfile)
    return result


@pytest.mark.parametrize("testname", TESTS)
def test_elimination(testname):
    "Tests elimination."
    aa, bb = get_test_input(testname)
    xx_expected = get_test_output(testname)
    if xx_expected is None:
        # Linear system of equations can not be solved -> expecting exception
        with pytest.raises(np.linalg.LinAlgError):
            solvers.gaussian_eliminate(aa, bb)
    else:
        xx_gauss = solvers.gaussian_eliminate(aa, bb)
        # Make sure, both vectors are row vectors so that they can be compared
        if len(xx_expected.shape) == 1:
            xx_expected.shape = (1, xx_expected.shape[0])
        xx_expected = xx_expected.transpose()
        xx_gauss.shape = (xx_gauss.shape[0], -1)
        assert np.allclose(xx_gauss, xx_expected, atol=ABSOLUTE_TOLERANCE,
                           rtol=RELATIVE_TOLERANCE)


if __name__ == '__main__':
    pytest.main()
