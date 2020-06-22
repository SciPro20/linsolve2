"""Routines for solving a linear system of equations."""
import numpy.linalg as linalg


def gaussian_eliminate(aa, bb):
    """Solves a linear system of equations (Ax = b) by Gauss-elimination

    Args:
        aa: Matrix with the coefficients. Shape: (n, n).
        bb: Right hand side of the equation. Shape: (n,)

    Returns:
        Vector xx with the solution of the linear equation.

    Raises:
        numpy.linalg.LinAlgError: if the system of equation is close to linear
            dependency.
    """
    xx = linalg.solve(aa, bb)
    return xx
