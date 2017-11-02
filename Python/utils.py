import numpy as np

def check_type(var, dtype):
    '''
    Verifies that `var` is of type `dtype`.

    Parameters
    ----------
    var
        Variable whose datatype is dubious.
    dtype
        Desired datatype of `var`.

    Raises
    ------
    TypeError
        If `dtype` is not a valid datatype.
        If `var` is not of type `dtype`.

    '''
    if type(dtype) != type:
        raise TypeError("{} is not a datatype."
                        .format(dtype))
    if not isinstance(var, dtype):
        raise TypeError("expected {} to be {}, but was {} instead"
                        .format(var, dtype, type(var)))

def check_dim(A: np.ndarray, dim: int):
    '''
    Verifies that np.ndarray `A` is of dimensionality `dim`.

    Parameters
    ----------
    A : np.ndarray
        Array whose dimensionality is dubious.
    dim : int
        Desired dimensionality of `A`.

    Raises
    ------
    TypeError
        If `A` is not a np.ndarray.
    ValueError
        If `A` is not of dimensionality `dim`.

    '''
    check_type(A, np.ndarray)
    if A.ndim != dim:
        raise ValueError("expected array of dimensionality {}, found dimensionality {} instead"
                         .format(dim, A.ndim))

def to_col(v: np.ndarray) -> np.ndarray:
    '''
    Reshapes `v` into a two-dimensional column vector.

    Parameters
    ----------
    v : np.ndarray
        Array to be reshaped.
        Can be any dimensionality, as long as only a single dimension has non-one length.

    Returns
    -------
    col_v : np.ndarray
        `v` reshaped as a two-dimensional column vector.

    Raises
    ------
    TypeError
        If `v` is not a np.ndarray.
    ValueError
        If `v` has multiple non-one dimensions.

    '''
    check_type(v, np.ndarray)
    if np.squeeze(v).ndim != 1:
        raise ValueError("unable to reshape into vector due to multiple non-one dimensions")
    return v.reshape((-1, 1))

def to_row(v: np.ndarray) -> np.ndarray:
    '''
    Reshapes `v` into a two-dimensional row vector.

    Parameters
    ----------
    v : np.ndarray
        Array to be reshaped.
        Can be any dimensionality, as long as only a single dimension has non-one length.

    Returns
    -------
    row_v : np.ndarray
        `v` reshaped as a two-dimensional row vector.

    Raises
    ------
    TypeError
        If `v` is not a np.ndarray.
    ValueError
        If `v` has multiple non-one dimensions.

    '''
    check_type(v, np.ndarray)
    if np.squeeze(v).ndim != 1:
        raise ValueError("unable to reshape into vector due to multiple non-one dimensions")
    return v.reshape((1, -1))
