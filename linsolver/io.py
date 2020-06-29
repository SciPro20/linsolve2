'''Input/output routines for the equation solver.'''
import numpy as np


_ERROR_PREFIX = "ERROR::"


def read_input(inputfile):
    '''Reads the input for the solver.

    Args:
        inputfile: Name of the input file.

    Returns:
        Tuple (A, b) containing the coefficient matrix A and RHS of the
        equation b.
    '''
    inparray = np.loadtxt(inputfile)
    ndim = inparray.shape[1]
    aa = np.array(inparray[0:ndim, 0:ndim])
    bb = np.array(inparray[ndim:, 0:ndim])
    return aa, bb.transpose()


def write_input(inputfile, aa, bb):
    '''Writes an input for the linsolve script

    Args:
        inputfile: Name of the input file to write.
        aa: Coefficient matrix
        bb: Array with the RHS-vectors (as column vectors)
    '''
    nvars = aa.shape[0]
    nrhs = bb.shape[1]
    buffer = np.empty((nvars + nrhs, nvars), dtype=float)
    buffer[:nvars, :] = aa
    buffer[nvars:, :] = bb.transpose()
    np.savetxt(inputfile, buffer)


def write_error(filename, errortype, errormsg):
    '''Writes an output file with an error message.

    Args:
        filename: Name of the file to write.
        errortype: Short string identifying the type of the error.
        errormsg: Longer string containing the error message.
    '''
    with open(filename, 'w') as fp:
        fp.write('{}{}: {}\n'.format(_ERROR_PREFIX, errortype, errormsg))


def write_result(filename, xx):
    '''Writes the result of the solver into a file.

    Args:
        filename: Name of the file where the results should be written to.
        xx: Solution vectors. Shape (n, nrhs) or (n,) where n is the dimension
            of the system and nrhs the nr. of right hand side vectors for
            which a solution had been calculated. (Each solution vector is
            a column vector.)
    '''
    xcol = xx.reshape((-1, 1)) if len(xx.shape) == 1 else xx
    xrow = xcol.transpose()
    np.savetxt(filename, xrow)


def read_result(resultfile):
    '''Reads the result written by the solver (used for testing).

    Args:
        resultfile: Result file to read.

    Returns:
        Result vector x or None, if the result file contained an error message.
    '''
    with open(resultfile, 'r') as fp:
        line = fp.readline()
    if line.startswith(_ERROR_PREFIX):
        xx = None
    else:
        xx = np.loadtxt(resultfile)
    return xx
